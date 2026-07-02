from langchain_core.documents import Document

from app.loaders.base_loader import BaseLoader


class TXTLoader(BaseLoader):
    def load(self, file_path: str):
        with open(file_path, encoding="utf-8") as file:
            text = file.read()

        return [
            Document(
                page_content=text,
                metadata={
                    "source": file_path
                }
            )
        ]