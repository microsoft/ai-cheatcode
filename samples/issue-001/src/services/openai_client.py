"""Azure OpenAI client for embeddings and RAG-based question answering."""

import logging
import os
from openai import AzureOpenAI


class OpenAIService:
    """Wraps Azure OpenAI for embedding generation and chat completion."""

    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_key=os.environ["AZURE_OPENAI_KEY"],
            api_version="2024-06-01",
        )
        self.chat_deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
        self.embedding_deployment = os.environ.get(
            "AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-ada-002"
        )

    def get_embedding(self, text: str) -> list[float]:
        """Generate an embedding vector for the given text."""
        # Truncate very long text to stay within model limits
        truncated = text[:8000]
        response = self.client.embeddings.create(
            input=truncated,
            model=self.embedding_deployment,
        )
        return response.data[0].embedding

    def generate_answer(self, system_prompt: str, context: str, question: str) -> str:
        """Generate an answer using RAG: system prompt + retrieved context + user question."""
        messages = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": (
                    f"Use the following document excerpts to answer the question. "
                    f"Cite the document name and page when referencing content.\n\n"
                    f"DOCUMENTS:\n{context}\n\n"
                    f"QUESTION: {question}"
                ),
            },
        ]

        response = self.client.chat.completions.create(
            model=self.chat_deployment,
            messages=messages,
            temperature=0.3,
            max_tokens=1500,
        )

        return response.choices[0].message.content
