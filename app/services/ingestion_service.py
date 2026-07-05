from app.services.chunk_service import ChunkService
from app.services.document_service import DocumentService
from app.vectorstore.chroma_service import ChromaService


class IngestionService:
    def __init__(self):
        self.document_service = DocumentService()
        self.chunk_service = ChunkService()
        self.vector_store = ChromaService()

    def ingest_document(self, file_path: str):
        documents = self.document_service.load_document(file_path)

        chunks = self.chunk_service.chunk_documents(documents)

        self.vector_store.add_documents(chunks)

        return chunks