from app.services.generate_service import GenerateService

service = GenerateService()

question = service.generate(
    "Señales de tránsito"
)

print(question)