"""Azure Blob Storage client for PDF file storage."""

import logging
import os
from azure.storage.blob import BlobServiceClient


class BlobService:
    """Upload and manage PDF files in Azure Blob Storage."""

    def __init__(self):
        account = os.environ["AZURE_STORAGE_ACCOUNT"]
        key = os.environ["AZURE_STORAGE_KEY"]
        self.connection_string = (
            f"DefaultEndpointsProtocol=https;"
            f"AccountName={account};"
            f"AccountKey={key};"
            f"EndpointSuffix=core.windows.net"
        )
        self.container = os.environ.get("PDF_CONTAINER", "pdfs")

    def upload_pdf(self, filename: str, content: bytes) -> str:
        """Upload a PDF to Blob Storage and return the blob URL."""
        blob_service = BlobServiceClient.from_connection_string(self.connection_string)
        container_client = blob_service.get_container_client(self.container)

        # Ensure container exists
        try:
            container_client.get_container_properties()
        except Exception:
            container_client.create_container()

        blob_client = container_client.get_blob_client(filename)
        blob_client.upload_blob(content, overwrite=True, content_settings=None)

        logging.info(f"Uploaded {filename} to {self.container}")
        return blob_client.url
