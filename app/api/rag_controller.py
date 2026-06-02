from fastapi import APIRouter

from app.models.request import QueryRequest
from app.core.rag_service import query_documents

router = APIRouter()


@router.post("/query")
def query(request: QueryRequest):

    results = query_documents(
        request.question,
        request.top_k
    )

    return results