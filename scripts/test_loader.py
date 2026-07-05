from app.services.ingestion_service import IngestionService

service = IngestionService()

chunks = service.ingest_document("documents/sample.pdf")

print()

print(f"Successfully stored {len(chunks)} chunks.")