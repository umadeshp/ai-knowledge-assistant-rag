from app.core.logging import logger
from app.loaders.factory import LoaderFactory


class DocumentService:
    @staticmethod
    def load_document(file_path: str):
        logger.info("Loading document: %s", file_path)

        loader = LoaderFactory.get_loader(file_path)

        documents = loader.load(file_path)

        logger.info("Loaded %d document(s)", len(documents))

        return documents