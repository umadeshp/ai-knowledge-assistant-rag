from app.services.chunk_service import ChunkService
from app.services.document_service import DocumentService

documents = DocumentService.load_document(
    "documents/sample.pdf"
)

chunk_service = ChunkService()

chunks = chunk_service.chunk_documents(documents)

print(f"\nTotal Chunks: {len(chunks)}\n")

for index, chunk in enumerate(chunks):
    print("=" * 60)
    print(f"Chunk {index + 1}")
    print("=" * 60)
    print(chunk.page_content[:300])
    print()
    print(chunk.metadata)
    print()