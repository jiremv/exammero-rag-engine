from app.services.generate_service import GenerateService

service = GenerateService()

question = service.generate_controlled(
    "PEATONES"
)

print(question)