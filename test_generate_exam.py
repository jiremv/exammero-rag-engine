from app.services.generate_service import GenerateService
from app.generators.exam_xml_generator import ExamXmlGenerator

service = GenerateService()

questions = service.generate_exam(
    "Señales de tránsito",
    20
)

generator = ExamXmlGenerator()

generator.save(
questions,
"senales_transito.xml"
)

print(
"Examen generado correctamente"
)
