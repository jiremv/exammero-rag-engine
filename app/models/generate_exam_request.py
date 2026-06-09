from pydantic import BaseModel

class GenerateExamRequest(
    BaseModel
):

    examenId: str

    cantidad: int = 10