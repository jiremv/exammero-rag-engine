import json
import re

from app.models.exam_question import ExamQuestion
from app.providers.ollama_provider import OllamaProvider


class GenerateService:

    def __init__(self):

        self.provider = OllamaProvider()

    def generate(
        self,
        tema: str
    ):

        response = self.provider.generate(
            tema
        )
        print("========== RESPUESTA OLLAMA ==========")
        print(response)
        print("======================================")
        try:

            data = json.loads(
                response
            )

        except Exception as e:

            print("\nERROR JSON:\n")
            print(response)

            raise e

        # Limpia prefijos tipo:
        # A) ...
        # B) ...
        # C) ...
        alternativas_limpias = []

        for opcion in data.get(
            "alternativas",
            []
        ):

            if not isinstance(
                opcion,
                str
            ):
                continue

            opcion = re.sub(
                r'^[A-Z]\)\s*',
                '',
                opcion
            )

            alternativas_limpias.append(
                opcion
            )

        data["alternativas"] = alternativas_limpias

        print(
            "ALTERNATIVAS:",
            data["alternativas"]
        )

        print(
            "TOTAL:",
            len(data["alternativas"])
        )

        if len( 
            data["alternativas"] 
        ) < 3:
        
            raise ValueError(
                "Pregunta inválida: menos de 3 alternativas"
            )

        return ExamQuestion(
            **data
        )

    def generate_exam(
        self,
        tema: str,
        cantidad: int
    ):

        questions = []

        for _ in range(cantidad):

            try:

                question = self.generate(
                    tema
                )

                questions.append(
                    question
                )

            except Exception as e:

                print(
                    f"Pregunta descartada: {e}"
                )

        return questions