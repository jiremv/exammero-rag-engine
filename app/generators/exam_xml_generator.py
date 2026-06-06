from app.generators.xml_generator import XmlGenerator


class ExamXmlGenerator:

    def __init__(self):

        self.question_generator = XmlGenerator()

    def generate(
        self,
        questions
    ):

        xml = ""

        for question in questions:

            xml += self.question_generator.generate(
                question
            )

            xml += "\n"

        return xml

    def save(
        self,
        questions,
        filename
    ):

        xml = self.generate(
            questions
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                xml
            )

        return filename