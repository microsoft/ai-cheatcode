"""PDF text extraction and chunking using PyPDF."""

import hashlib
import logging
from io import BytesIO
from pypdf import PdfReader

# Target ~500 tokens per chunk, with 50-token overlap for context continuity
CHUNK_SIZE = 2000  # characters (~500 tokens)
CHUNK_OVERLAP = 200  # characters (~50 tokens)


class PDFProcessor:
    """Extract text from PDFs and split into overlapping chunks for indexing."""

    def extract_and_chunk(self, pdf_bytes: bytes, filename: str) -> list[dict]:
        """
        Extract text from a PDF and return a list of chunk dicts ready for indexing.

        Each chunk contains:
          - id: unique hash of filename + chunk position
          - content: the text chunk
          - filename: source PDF name
          - page: page number(s) the chunk spans
          - chunk_index: sequential chunk number
        """
        reader = PdfReader(BytesIO(pdf_bytes))
        pages = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            if text.strip():
                pages.append({"page_num": i + 1, "text": text})

        if not pages:
            logging.warning(f"No text extracted from {filename}")
            return []

        # Build chunks with page tracking
        chunks = []
        full_text = ""
        page_boundaries = []  # (char_offset, page_num)

        for p in pages:
            page_boundaries.append((len(full_text), p["page_num"]))
            full_text += p["text"] + "\n"

        # Sliding window chunking
        start = 0
        chunk_index = 0
        while start < len(full_text):
            end = min(start + CHUNK_SIZE, len(full_text))

            # Try to break at a sentence boundary
            if end < len(full_text):
                last_period = full_text.rfind(".", start, end)
                last_newline = full_text.rfind("\n", start, end)
                break_point = max(last_period, last_newline)
                if break_point > start + CHUNK_SIZE // 2:
                    end = break_point + 1

            chunk_text = full_text[start:end].strip()
            if not chunk_text:
                start = end
                continue

            # Determine which pages this chunk spans
            chunk_pages = set()
            for offset, page_num in page_boundaries:
                if offset <= end and offset + len(pages[page_num - 1]["text"]) >= start:
                    chunk_pages.add(page_num)

            page_label = ", ".join(str(p) for p in sorted(chunk_pages)) if chunk_pages else "1"

            chunk_id = hashlib.md5(f"{filename}:{chunk_index}".encode()).hexdigest()

            chunks.append({
                "id": chunk_id,
                "content": chunk_text,
                "filename": filename,
                "page": page_label,
                "chunk_index": chunk_index,
            })

            chunk_index += 1
            start = end - CHUNK_OVERLAP  # Overlap for context

        logging.info(f"Created {len(chunks)} chunks from {filename} ({len(pages)} pages)")
        return chunks
