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
      "texto alternativa",
      "texto alternativa",
      "texto alternativa",
      "texto alternativa"
  ],
  "correcta":0,
  "explicacion":"explicacion de la respuesta"
}}

- La pregunta debe estar relacionada estrictamente con: {tema}
- NO colocar A), B), C), D).
- correcta es el índice empezando en 0.
- No inventar temas ajenos al solicitado.
- Debe existir una única respuesta correcta.
- Las alternativas incorrectas deben ser plausibles.
- Todas las alternativas deben tener longitud similar.
- explicacion es obligatoria.
- explicacion debe explicar por qué la respuesta correcta es válida.
- explicacion debe tener entre 20 y 100 palabras.
- Responder únicamente JSON.
- No escribas markdown.
- No escribas comentarios.

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