"""Azure AI Search client for index management and hybrid search."""

import logging
import os
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
)
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential


class SearchService:
    """Manages the Azure AI Search index and performs hybrid search."""

    def __init__(self):
        self.endpoint = os.environ["AZURE_SEARCH_ENDPOINT"]
        self.key = os.environ["AZURE_SEARCH_KEY"]
        self.index_name = os.environ.get("AZURE_SEARCH_INDEX", "pdf-documents")
        self.credential = AzureKeyCredential(self.key)

    def _get_index_client(self) -> SearchIndexClient:
        return SearchIndexClient(self.endpoint, self.credential)

    def _get_search_client(self) -> SearchClient:
        return SearchClient(self.endpoint, self.index_name, self.credential)

    def ensure_index_exists(self):
        """Create the search index if it doesn't exist."""
        client = self._get_index_client()

        try:
            client.get_index(self.index_name)
            logging.info(f"Index '{self.index_name}' already exists")
            return
        except Exception:
            pass

        logging.info(f"Creating index '{self.index_name}'")

        fields = [
            SimpleField(name="id", type=SearchFieldDataType.String, key=True),
            SearchableField(name="content", type=SearchFieldDataType.String),
            SimpleField(
                name="filename",
                type=SearchFieldDataType.String,
                filterable=True,
                facetable=True,
            ),
            SimpleField(name="page", type=SearchFieldDataType.String, filterable=True),
            SimpleField(
                name="chunk_index",
                type=SearchFieldDataType.Int32,
                sortable=True,
            ),
            SearchField(
                name="embedding",
                type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                searchable=True,
                vector_search_dimensions=1536,
                vector_search_profile_name="default-profile",
            ),
        ]

        vector_search = VectorSearch(
            algorithms=[HnswAlgorithmConfiguration(name="default-algorithm")],
            profiles=[
                VectorSearchProfile(
                    name="default-profile",
                    algorithm_configuration_name="default-algorithm",
                )
            ],
        )

        index = SearchIndex(
            name=self.index_name,
            fields=fields,
            vector_search=vector_search,
        )

        client.create_index(index)
        logging.info(f"Index '{self.index_name}' created")

    def upload_documents(self, chunks: list[dict]):
        """Upload document chunks to the search index."""
        client = self._get_search_client()
        # Upload in batches of 100
        batch_size = 100
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i : i + batch_size]
            client.upload_documents(documents=batch)
            logging.info(f"Uploaded batch {i // batch_size + 1} ({len(batch)} docs)")

    def search(
        self, query: str, query_embedding: list[float], top: int = 5
    ) -> list[dict]:
        """Hybrid search: combines text search with vector similarity."""
        client = self._get_search_client()

        vector_query = VectorizedQuery(
            vector=query_embedding,
            k_nearest_neighbors=top,
            fields="embedding",
        )

        results = client.search(
            search_text=query,
            vector_queries=[vector_query],
            top=top,
            select=["id", "content", "filename", "page", "chunk_index"],
        )

        hits = []
        for r in results:
            hits.append({
                "id": r["id"],
                "content": r["content"],
                "filename": r["filename"],
                "page": r["page"],
                "score": r["@search.score"],
            })

        return hits

    def get_index_stats(self) -> dict:
        """Return document count and storage size for the index."""
        client = self._get_index_client()
        try:
            stats = client.get_index_statistics(self.index_name)
            return {
                "document_count": stats.document_count,
                "storage_size": stats.storage_size,
            }
        except Exception:
            return {"document_count": 0, "storage_size": 0}
