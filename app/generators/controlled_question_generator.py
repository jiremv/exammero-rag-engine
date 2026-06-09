import random

from app.models.exam_question import ExamQuestion
from app.shards.manejo.manejo_shard import (
    ManejoShard
)

class ControlledQuestionGenerator:

    DISTRACTORES = [
        "Adelantar a otro vehículo",
        "Aumentar la velocidad",
        "Continuar sin detenerse",
        "Girar obligatoriamente a la derecha",
        "Reducir la velocidad a 20 km/h",
        "Estacionar en cualquier lugar",
        "Ignorar la señalización",
        "Circular por el carril contrario"
    ]

    def __init__(self):
        self.shard = ManejoShard()

    def limpiar_concepto(
        self,
        texto: str
    ):

        return (
            texto
            .replace("La señal", "")
            .replace("La luz", "")
            .replace("El semáforo", "")            
            .strip()
        )    

    def generate(
        self,
        fragmento: str
    ):

        texto = fragmento.strip()

        if " indica " in texto:

            partes = texto.split(
                " indica ",
                1
            )

            concepto = self.limpiar_concepto(
                partes[0]
            )

            significado = partes[1].strip(". ")

            pregunta = (
                f"¿Qué indica la señal {concepto}?"
            )

        elif " tiene prioridad " in texto:

            significado = texto.strip(". ")

            pregunta = (
                "¿Quién tiene prioridad?"
            )

        elif " obliga " in texto:

            partes = texto.split(
                " obliga ",
                1
            )

            concepto = self.limpiar_concepto(
                partes[0]
            )

            significado = partes[1].strip(". ")

            pregunta = (
                f"¿Qué obliga a hacer la señal {concepto}?"
            )

        elif " advierte " in texto:

            partes = texto.split(
                " advierte ",
                1
            )

            concepto = self.limpiar_concepto(
                partes[0]
            )

            significado = partes[1].strip(". ")

            pregunta = (
                f"¿Qué advierte la señal {concepto}?"
            )

        elif " permite " in texto:

            partes = texto.split(
                " permite ",
                1
            )

            concepto = self.limpiar_concepto(
                partes[0]
            )

            significado = partes[1].strip(". ")

            pregunta = (
                f"¿Qué permite la señal {concepto}?"
            )

        elif " prohíbe " in texto:

            partes = texto.split(
                " prohíbe ",
                1
            )

            concepto = self.limpiar_concepto(
                partes[0]
            )

            significado = partes[1].strip(". ")

            pregunta = (
                f"¿Qué prohíbe la señal {concepto}?"
            )

        elif texto.startswith(
            "Está prohibido"
        ):

            significado = texto.strip(". ")

            pregunta = (
                "¿Qué acción no está permitida según la norma de tránsito?"
            )
            
        elif "prioridad de paso" in texto:

            significado = texto.strip(". ")

            pregunta = (
                "¿Quién tiene prioridad de paso?"
            )

        else:

            pregunta = (
                "¿Qué indica la siguiente señal o regla?"
            )

            significado = texto


        significado = (
            significado
            .replace("al conductor a ", "")
            .replace("que ", "")
            .strip()
        )

        fragmentos = (
            self.shard.get_random_fragments(
                10
            )
        )

        distractores = []

        for frag in fragmentos:

            if frag == texto:
                continue

            distractor = (
                self.extraer_significado(
                    frag
                )
            )

            if distractor != significado:

                distractores.append(
                    distractor
                )

            if len(
                distractores
            ) == 3:

                break

        alternativas = [
            significado
        ] + distractores

        random.shuffle(
            alternativas
        )

        correcta = alternativas.index(
            significado
        )

        return ExamQuestion(
            q0="",
            g0="",
            q=pregunta,
            q2="",
            q3="",
            q4="",
            q5="",
            alternativas=alternativas,
            correcta=correcta,
            explicacion=(
                f"La alternativa correcta es "
                f"'{significado}' porque "
                f"{texto}"
            )
        )

    def limpiar_significado(
        self,
        texto: str
    ):

        return (
            texto
            .replace("al conductor a ", "")
            .replace("al conductor que ", "")
            .replace("que ", "")
            .strip()
        )        

    def extraer_significado(
        self,
        texto: str
    ):

        if " indica " in texto:

            return self.limpiar_significado(
                texto.split(
                    " indica ",
                    1
                )[1].strip(". ")
            )

        if " obliga " in texto:

            return self.limpiar_significado(
                texto.split(
                    " obliga ",
                    1
                )[1].strip(". ")
            )

        if " advierte " in texto:

            return self.limpiar_significado(
                texto.split(
                    " advierte ",
                    1
                )[1].strip(". ")
            )

        if " permite " in texto:

            return self.limpiar_significado(
                texto.split(
                    " permite ",
                    1
                )[1].strip(". ")
            )

        return texto        