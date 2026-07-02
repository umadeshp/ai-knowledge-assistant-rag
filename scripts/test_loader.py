from app.services.document_service import DocumentService

documents = DocumentService.load_document(
    "documents/sample.docx"
)

print("=" * 50)

print(documents[0].page_content[:1000])

print("=" * 50)

print(documents[0].metadata)