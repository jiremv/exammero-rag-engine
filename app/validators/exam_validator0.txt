class ExamValidator:

    def validate(
        self,
        question
    ):

        errores = []

        if len(question.alternativas) < 3:
            errores.append(
                "Menos de 3 alternativas"
            )

        if question.correcta < 0:
            errores.append(
                "Respuesta correcta negativa"
            )

        if question.correcta >= len(
            question.alternativas
        ):
            errores.append(
                "Índice de respuesta inválido"
            )

        if not question.explicacion:
            errores.append(
                "Explicación vacía"
            )

        return errores