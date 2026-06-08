from pydantic import BaseModel


class GenerateRequest(BaseModel):

    tema: str