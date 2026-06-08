from pydantic import BaseModel


class GenerateExamRequest(BaseModel):

    tema: str

    cantidad: int = 10