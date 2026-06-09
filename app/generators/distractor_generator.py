from ollama import chat
import json


class DistractorGenerator:

    def generate(
        self,
        correcta: str
    ):

        prompt = f"""
Genera exactamente 3 distractores para una pregunta de examen de manejo.

Respuesta correcta:

{correcta}

Reglas:

* Los distractores deben ser plausibles.
* No repetir la respuesta correcta.
* No explicar.
* Responder únicamente JSON.

Formato:

[
"texto",
"texto",
"texto"
]
"""

        response = chat(
            model="llama3.2:3b",
            format="json",
            options={
                "temperature": 0.4
            },
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        try:

            distractores = json.loads(
                response["message"]["content"]
            )

            if len(distractores) >= 3:

                return distractores[:3]

        except Exception:

            pass

        return [
            "Está permitido adelantar",
            "Es obligatorio aumentar la velocidad",
            "No existe ninguna restricción"
        ]