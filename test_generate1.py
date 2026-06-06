from app.services.generate_service import GenerateService
from app.generators.xml_generator import XmlGenerator

service = GenerateService()

question = service.generate(
    "Señales de tránsito"
)

generator = XmlGenerator()

xml = generator.generate(
    question
)

print(xml)