from app.services.generate_service import (
    GenerateService
)

from app.generators.exam_xml_generator import (
    ExamXmlGenerator
)

service = GenerateService()

questions = service.generate_exam(
    "manejo",
    20
)

print(
    f"TOTAL PREGUNTAS: {len(questions)}"
)

generator = ExamXmlGenerator()

xml = generator.generate(
    questions
)

print(xml)