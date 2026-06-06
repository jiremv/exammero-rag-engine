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

        data = json.loads(
            response
        )

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