from app.vectorstore.chroma_service import ChromaService

db = ChromaService()

results = db.similarity_search(
    "Tell me about Python."
)

print()

for index, doc in enumerate(results):

    print("=" * 60)

    print(index + 1)

    print(doc.page_content[:300])

    print()

    print(doc.metadata)