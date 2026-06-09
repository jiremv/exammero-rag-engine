from app.generators.controlled_question_generator import (
    ControlledQuestionGenerator
)

from app.providers.context_provider import (
    ContextProvider
)

from app.validators.exam_validator import (
    ExamValidator
)

from app.validators.semantic_validator import (
    SemanticValidator
)


class GenerateService:

    def __init__(self):

        self.provider = ContextProvider()

        self.generator = (
            ControlledQuestionGenerator()
        )
        self.usados = set()

    def generate(
        self,
        tema: str
    ):

        exam_validator = ExamValidator()

        semantic_validator = SemanticValidator()

        for _ in range(5):

            fragmento = None

            for _ in range(20):

                candidato = (
                    self.provider.search_random()
                )

                if candidato not in self.usados:

                    self.usados.add(
                        candidato
                    )

                    fragmento = candidato

                    break

            if fragmento is None:

                return None

            question = (
                self.generator.generate(
                    fragmento
                )
            )

            errors = []

            errors.extend(
                exam_validator.validate(
                    question
                )
            )

            errors.extend(
                semantic_validator.validate(
                    question
                )
            )

            if not errors:

                return question

            print(
                f"Pregunta descartada: {errors}"
            )

        raise ValueError(
            "No se pudo generar una pregunta válida"
        )

    def generate_exam(
        self,
        tema: str,
        cantidad: int
    ):
        self.usados.clear()

        questions = []

        for _ in range(cantidad):

            try:

                question = self.generate(
                    tema
                )
                if question is None:
                    break
                questions.append(
                    question
                )

            except Exception as e:

                print(
                    f"Pregunta descartada: {e}"
                )

        return questions