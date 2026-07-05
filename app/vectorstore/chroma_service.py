from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings


class ChromaService:
    def __init__(self):
        self.embedding_function = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.db = Chroma(
            collection_name="knowledge_base",
            embedding_function=self.embedding_function,
            persist_directory="chroma_db",
        )

    def add_documents(self, documents: list[Document]):
        self.db.add_documents(documents)

    def similarity_search(self, query: str, k: int = 4):
        return self.db.similarity_search(query, k=k)