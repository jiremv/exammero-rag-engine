from app.services.generate_service import GenerateService
from app.generators.xml_generator import XmlGenerator
from app.validators.exam_validator import ExamValidator

service = GenerateService()

question = service.generate(
    "Señales de tránsito"
)

validator = ExamValidator()

errores = validator.validate(
    question
)

print("ERRORES:", errores)

if errores:
    print("La pregunta generada no es válida")
else:

    generator = XmlGenerator()

    xml = generator.generate(
        question
    )

    print(xml)