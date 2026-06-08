from fastapi import APIRouter, Response

from app.generators.exam_xml_generator import ExamXmlGenerator
from app.generators.xml_generator import XmlGenerator
from app.models.generate_exam_request import GenerateExamRequest
from app.models.generate_request import GenerateRequest
from app.services.generate_service import GenerateService

router = APIRouter()

service = GenerateService()


@router.post("/generate-question")
def generate_question(
    request: GenerateRequest
):

    question = service.generate(
        request.tema
    )

    return question


@router.post("/generate-question-xml")
def generate_question_xml(
    request: GenerateRequest
):

    question = service.generate(
        request.tema
    )

    generator = XmlGenerator()

    xml = generator.generate(
        question
    )

    return Response(
        content=xml,
        media_type="application/xml"
    )


@router.post("/generate-exam")
def generate_exam(
    request: GenerateExamRequest
):

    questions = service.generate_exam(
        request.tema,
        request.cantidad
    )

    return questions


@router.post("/generate-exam-xml")
def generate_exam_xml(
    request: GenerateExamRequest
):

    questions = service.generate_exam(
        request.tema,
        request.cantidad
    )

    generator = ExamXmlGenerator()

    xml = generator.generate(
        questions
    )

    return Response(
        content=xml,
        media_type="application/xml"
    )