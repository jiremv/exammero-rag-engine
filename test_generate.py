from app.services.generate_service import (
    GenerateService
)

from app.generators.xml_generator import (
    XmlGenerator
)

service = GenerateService()

question = service.generate(
    "PEATONES"
)

print("\nPREGUNTA:\n")
print(question.q)

print("\nALTERNATIVAS:\n")

for i, a in enumerate(
    question.alternativas
):
    print(i, a)

print(
    "\nCORRECTA:",
    question.correcta
)

print(
    "\nEXPLICACION:\n"
)

print(
    question.explicacion
)

generator = XmlGenerator()

xml = generator.generate(
    question
)

print(
    "\nXML GENERADO:\n"
)

print(xml)