class XmlGenerator:
    
    LETRAS = ["A", "B", "C", "D", "E", "F"]

    def generate(
        self,
        question
    ):

        letra_correcta = self.LETRAS[
            question.correcta
        ]

        xml = f"""
<p xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:noNamespaceSchemaLocation="./../../../clase.xsd">

    <q0>{question.q0}</q0>

    <g0>{question.g0}</g0>

    <q>{question.q}</q>

    <q2>{question.q2}</q2>

    <q3>{question.q3}</q3>

    <q4>{question.q4}</q4>

    <q5>{question.q5}</q5>

    <as r="R" correcta="{question.correcta}">
"""

        for opcion in question.alternativas:
            xml += f"\n        <a>{opcion}</a>"

        xml += f"""

    </as>

    <x>{letra_correcta}.</x>

    <x2>{question.explicacion}</x2>

    <i></i>

    <i2></i2>

    <v1></v1>

</p>
"""

        return xml