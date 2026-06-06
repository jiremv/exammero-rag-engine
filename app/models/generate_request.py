from pydantic import BaseModel


class GenerateRequest(BaseModel):

    tema: str

    cantidad: int = 5

    nivel: str = "basico"