from ollama import chat

from app.shards.manejo.manejo_shard import ManejoShard

class OllamaProvider:

    def __init__(self):

        self.shard = ManejoShard()

    def generate(
        self,
        tema: str
    ):

        contexto = self.shard.search(
            tema
        )

        prompt = f"""

Contexto:

{contexto}

Genera una pregunta de examen utilizando únicamente la información del contexto.

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

Reglas:

* NO generes preguntas sobre el mismo concepto si ya fue utilizado anteriormente.
* Selecciona aleatoriamente un fragmento distinto del contexto recuperado.
* Las cuatro alternativas deben ser plausibles.
* Utiliza una parte distinta del contexto.
* No repitas preguntas previamente generadas.
* Si existen varias señales o reglas en el contexto, elige una diferente para cada pregunta.
* Genera exactamente 4 alternativas.
* No inventes información.
* No uses conocimientos externos.
* Debe existir una única respuesta correcta.
* NO colocar A), B), C), D).
* correcta es el índice empezando en 0.
* explicacion es obligatoria.
* Responder únicamente JSON.
  """
        response = chat(
            model="llama3.2:3b",
            format="json",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]
