from app.services.retrieval_service import RetrievalService

rag = RetrievalService()

response = rag.ask(
    "What programming languages does Uma know?"
)

print()

print("=" * 60)

print("ANSWER")

print("=" * 60)

print(response["answer"])

print()

print("=" * 60)

print("SOURCES")

print("=" * 60)

for source in response["sources"]:
    print(source)