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
        #data = json.loads(
        #    response
        #)

        # Limpia prefijos tipo:
        # A) ...
        # B) ...
        # C) ...
        for i, opcion in enumerate(
            data["alternativas"]
        ):

            opcion = re.sub(
                r'^[A-Z]\)\s*',
                '',
                opcion
            )

            data["alternativas"][i] = opcion

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

            question = self.generate(
                tema
            )

            questions.append(
                question
            )

        return questions