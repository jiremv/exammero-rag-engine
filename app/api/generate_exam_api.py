from fastapi import APIRouter
from pydantic import BaseModel

from app.services.generate_service import (
    GenerateService
)

from app.generators.xml_generator import (
    XmlGenerator
)

from app.services.s3_service import (
    S3Service
)

router = APIRouter()


class GenerateExamRequest(
    BaseModel
):

    examenId: str
    cantidad: int


@router.post(
    "/generate-exam"
)
def generate_exam(
    request: GenerateExamRequest
):

    print(
        f"🤖 Generando examen IA: "
        f"{request.examenId}"
    )

    service = GenerateService()

    xml_generator = XmlGenerator()

    s3 = S3Service()

    questions = service.generate_exam(
        request.examenId,
        request.cantidad
    )

    uploaded = []

    for index, question in enumerate(
        questions,
        start=1
    ):

        xml = xml_generator.generate(
            question
        )

        key = s3.upload_xml(
            request.examenId,
            index,
            xml
        )

        uploaded.append(
            key
        )

        print(
            f"✅ XML SUBIDO: {key}"
        )

    return {
        "ok": True,
        "cantidad": len(uploaded),
        "files": uploaded
    }