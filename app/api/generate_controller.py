from fastapi import APIRouter

from app.models.generate_request import GenerateRequest
from app.services.generate_service import GenerateService

router = APIRouter()

service = GenerateService()


@router.post("/generate")
def generate(
    request: GenerateRequest
):

    return service.generate(
        request.tema,
        request.cantidad,
        request.nivel
    )