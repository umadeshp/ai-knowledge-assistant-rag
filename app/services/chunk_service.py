from pathlib import Path

from app.core.logging import logger
from app.rag.chunker import DocumentChunker


class ChunkService:
    def __init__(self):
        self.chunker = DocumentChunker()

    def chunk_documents(self, documents):
        logger.info("Starting document chunking...")

        chunks = self.chunker.split_documents(documents)

        logger.info("Created %d chunks", len(chunks))

        for index, chunk in enumerate(chunks):
            chunk.metadata["chunk_id"] = index

            source = chunk.metadata.get("source", "")
            chunk.metadata["document_name"] = Path(source).name

        return chunks