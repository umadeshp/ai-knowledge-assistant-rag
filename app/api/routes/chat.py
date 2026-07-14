from fastapi import APIRouter

from app.services.retrieval_service import RetrievalService

router = APIRouter()

service = RetrievalService()


@router.post("/chat")
def chat(question: str):
    return service.ask(question)