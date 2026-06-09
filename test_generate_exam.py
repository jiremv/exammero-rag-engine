from app.services.generate_service import GenerateService
from app.generators.exam_xml_generator import ExamXmlGenerator

service = GenerateService()

temas = [
    "PARE",
    "CEDA EL PASO",
    "CALZADA RESBALADIZA",
    "DOBLE SENTIDO",
    "PROHIBIDO ADELANTAR",
    "SEMAFORO",
    "PEATONES",
    "VELOCIDAD"
]

questions = service.generate_exam(
    "Señales de tránsito",
    50
)

generator = ExamXmlGenerator()

generator.save(
questions,
"senales_transito.xml"
)

print(
"Examen generado correctamente"
)
