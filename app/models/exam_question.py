from pydantic import BaseModel
from typing import List


class ExamQuestion(BaseModel):

    q0: str = ""

    g0: str = ""

    q: str

    q2: str = ""

    q3: str = ""

    q4: str = ""

    q5: str = ""

    alternativas: List[str]

    correcta: int

    explicacion: str = ""