from app.validators.semantic_validator import SemanticValidator

validator = SemanticValidator()

errores = validator.validate(
    question
)

print(
    "ERRORES:",
    errores
)
