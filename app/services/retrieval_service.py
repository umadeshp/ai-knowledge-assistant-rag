from app.llm.openai_service import OpenAIService
from app.vectorstore.chroma_service import ChromaService


class RetrievalService:

    def __init__(self):
        self.vector_store = ChromaService()
        self.llm = OpenAIService()

    def ask(self, question: str):

        documents = self.vector_store.similarity_search(
            question,
            k=4,
        )

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        answer = self.llm.generate_answer(
            context=context,
            question=question,
        )

        return {
            "question": question,
            "answer": answer,
            "sources": [
                doc.metadata
                for doc in documents
            ],
        }