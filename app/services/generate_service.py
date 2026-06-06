from ollama import chat


class GenerateService:

    def generate(
        self,
        tema: str,
        cantidad: int,
        nivel: str
    ):

        prompt = f"""
Genera {cantidad} preguntas de examen sobre {tema}.

Nivel: {nivel}

Devuelve únicamente JSON válido con esta estructura:

[
  {{
    "q": "pregunta",
    "opciones": [
      "A",
      "B",
      "C",
      "D"
    ],
    "correcta": 0,
    "explicacion": "..."
  }}
]
"""

        response = chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]