import boto3


class S3Service:

    def __init__(self):

        self.bucket = (
            "examensolucion-bucket"
        )

        self.s3 = boto3.client(
            "s3"
        )

    def upload_xml(
        self,
        examen_id: str,
        numero: int,
        xml: str
    ):

        key = (
            f"preguntas/nom/"
            f"{examen_id}/"
            f"{numero}.xml"
        )

        self.s3.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=xml.encode(
                "utf-8"
            ),
            ContentType="application/xml"
        )

        print(
            f"🚀 SUBIDO A S3: {key}"
        )

        return key