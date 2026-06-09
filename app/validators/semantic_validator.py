class SemanticValidator:

    def validate(
        self,
        question
    ):

        errors = []

        if (
            question.correcta < 0 or
            question.correcta >= len(question.alternativas)
        ):
            errors.append(
                "Índice de respuesta inválido"
            )
            return errors

        pregunta = question.q.lower().strip()
        explicacion = question.explicacion.lower().strip()

        respuesta_correcta = (
            question.alternativas[
                question.correcta
            ]
        )

        respuesta = respuesta_correcta.lower().strip()

        if "pregunta principal" in pregunta:

            errors.append(
                "Plantilla no reemplazada"
            )

        temas_prohibidos = [
            "gafas",
            "radiación uv",
            "contactos",
            "medicina",
            "salud ocular"
        ]

        for tema in temas_prohibidos:

            if tema in pregunta or tema in explicacion:

                errors.append(
                    "Tema fuera del contexto de manejo"
                )

        if len(explicacion) < 30:

            errors.append(
                "Explicación demasiado corta"
            )

        if not respuesta:

            errors.append(
                "Respuesta correcta vacía"
            )

        if respuesta not in explicacion:

            palabras = [
                palabra
                for palabra in respuesta.split()
                if len(palabra) > 4
            ]

            coincidencias = 0

            for palabra in palabras:

                if palabra in explicacion:

                    coincidencias += 1

            if coincidencias < 2:

                errors.append(
                    "La explicación no parece justificar la respuesta correcta"
                )

        if (
            "ambos sentidos" in explicacion
            and "una dirección" in respuesta
        ):

            errors.append(
                "Respuesta contradice explicación"
            )

        if (
            "baja adherencia" in explicacion
            and (
                "cerrada" in respuesta or
                "estacionamiento" in respuesta or
                "un sentido" in respuesta
            )
        ):

            errors.append(
                "Respuesta contradice explicación"
            )
          

        if len(question.q.strip()) < 10:
            errors.append(
                "Pregunta demasiado corta"
            )

        for alternativa in question.alternativas:

            if len(alternativa.strip()) < 5:

                errors.append(
                    "Alternativa demasiado corta"
                )
        return errors