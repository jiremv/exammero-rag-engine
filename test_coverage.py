from app.services.generate_service import (
    GenerateService
)

service = GenerateService()

questions = service.generate_exam(
    "manejo",
    40
)

print(
    "GENERADAS:",
    len(questions)
)

print(
    "UNIQUE:",
    len(
        set(
            q.explicacion
            for q in questions
        )
    )
)