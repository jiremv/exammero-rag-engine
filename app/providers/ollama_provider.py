from ollama import chat


class OllamaProvider:

    def generate(
        self,
        tema: str
    ):

        prompt = f"""
Genera una pregunta de examen sobre:

{tema}

Devuelve únicamente JSON válido.

Formato:

{{
  "q0":"",
  "g0":"",
  "q":"Pregunta principal",
  "q2":"",
  "q3":"",
  "q4":"",
  "q5":"",
  "alternativas":[
      "A",
      "B",
      "C",
      "D"
  ],
  "correcta":0,
  "explicacion":""
}}

No escribas markdown.
No escribas comentarios.
"""

        response = chat(
            model='llama3',
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )

        return response['message']['content']