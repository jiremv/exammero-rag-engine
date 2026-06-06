import json

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

        data = json.loads(response)

        return ExamQuestion(**data)