"""
PDF Document Analysis Agent — Azure Functions Application

Issue #001: Code-First Agent Delivery
The Ch(e)at Code — ABS Tech Strategy

Three endpoints:
  POST /api/upload    — Upload and index a PDF
  POST /api/query     — Ask questions about indexed documents
  GET  /api/status    — Check index health and document count
"""

import azure.functions as func
import json
import logging
import os

from services.pdf_processor import PDFProcessor
from services.search_client import SearchService
from services.openai_client import OpenAIService
from services.blob_client import BlobService

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

pdf_processor = PDFProcessor()
search_service = SearchService()
openai_service = OpenAIService()
blob_service = BlobService()

SYSTEM_PROMPT = """You are a document analysis assistant specialized in processing large PDF documents.

When answering questions:
1. Cite the specific document name and section when referencing content.
2. If a question cannot be answered from the available documents, say so clearly.
3. When comparing across documents, structure your response as a clear comparison.
4. Flag any contradictions or inconsistencies between documents.
5. For compliance-related questions, recommend human review for final decisions."""


@app.route(route="upload", methods=["POST"])
async def upload_pdf(req: func.HttpRequest) -> func.HttpResponse:
    """Upload a PDF, chunk it, generate embeddings, and index into Azure AI Search."""
    logging.info("PDF upload request received")

    try:
        # Get the uploaded file
        file = req.files.get("file")
        if not file:
            body = req.get_body()
            if not body:
                return func.HttpResponse(
                    json.dumps({"error": "No file provided. Send a PDF as multipart/form-data with key 'file'."}),
                    status_code=400,
                    mimetype="application/json",
                )
            file_content = body
            filename = req.params.get("filename", "uploaded.pdf")
        else:
            file_content = file.read()
            filename = file.filename

        if not filename.lower().endswith(".pdf"):
            return func.HttpResponse(
                json.dumps({"error": "Only PDF files are supported."}),
                status_code=400,
                mimetype="application/json",
            )

        # 1. Store the original PDF in Blob Storage
        blob_url = blob_service.upload_pdf(filename, file_content)
        logging.info(f"PDF stored at: {blob_url}")

        # 2. Extract text and chunk the PDF
        chunks = pdf_processor.extract_and_chunk(file_content, filename)
        logging.info(f"Extracted {len(chunks)} chunks from {filename}")

        # 3. Generate embeddings for each chunk
        for chunk in chunks:
            chunk["embedding"] = openai_service.get_embedding(chunk["content"])

        # 4. Ensure search index exists, then upload chunks
        search_service.ensure_index_exists()
        search_service.upload_documents(chunks)
        logging.info(f"Indexed {len(chunks)} chunks into Azure AI Search")

        return func.HttpResponse(
            json.dumps({
                "status": "success",
                "filename": filename,
                "chunks_indexed": len(chunks),
                "blob_url": blob_url,
            }),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Upload failed: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": f"Upload failed: {str(e)}"}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="query", methods=["POST"])
async def query_documents(req: func.HttpRequest) -> func.HttpResponse:
    """Ask a question about indexed PDF documents using RAG."""
    logging.info("Query request received")

    try:
        body = req.get_json()
        question = body.get("question")
        if not question:
            return func.HttpResponse(
                json.dumps({"error": "Provide a 'question' field in the JSON body."}),
                status_code=400,
                mimetype="application/json",
            )

        # 1. Generate embedding for the question
        question_embedding = openai_service.get_embedding(question)

        # 2. Search for relevant chunks (hybrid: text + vector)
        results = search_service.search(question, question_embedding, top=5)

        if not results:
            return func.HttpResponse(
                json.dumps({
                    "answer": "No relevant documents found. Please upload PDFs first using the /api/upload endpoint.",
                    "sources": [],
                }),
                status_code=200,
                mimetype="application/json",
            )

        # 3. Build context from search results
        context_parts = []
        sources = []
        for r in results:
            context_parts.append(f"[{r['filename']} — Page {r['page']}]\n{r['content']}")
            sources.append({"filename": r["filename"], "page": r["page"], "score": r["score"]})

        context = "\n\n---\n\n".join(context_parts)

        # 4. Generate answer using Azure OpenAI
        answer = openai_service.generate_answer(SYSTEM_PROMPT, context, question)

        return func.HttpResponse(
            json.dumps({
                "answer": answer,
                "sources": sources,
                "chunks_searched": len(results),
            }),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        logging.error(f"Query failed: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": f"Query failed: {str(e)}"}),
            status_code=500,
            mimetype="application/json",
        )


@app.route(route="status", methods=["GET"])
async def check_status(req: func.HttpRequest) -> func.HttpResponse:
    """Check the health of the search index and return document count."""
    try:
        stats = search_service.get_index_stats()
        return func.HttpResponse(
            json.dumps({
                "status": "healthy",
                "index_name": os.environ.get("AZURE_SEARCH_INDEX", "pdf-documents"),
                "document_count": stats.get("document_count", 0),
                "storage_size_bytes": stats.get("storage_size", 0),
            }),
            status_code=200,
            mimetype="application/json",
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"status": "error", "message": str(e)}),
            status_code=500,
            mimetype="application/json",
        )
