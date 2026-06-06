import chromadb

from pathlib import Path
from ollama import embeddings


client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="manejo"
)

base_path = Path(
    "datasets/manejo"
)

for file in base_path.glob("*.txt"):

    content = file.read_text(
        encoding="utf-8"
    )

    chunks = [
        chunk.strip()
        for chunk in content.split("\n\n")
        if chunk.strip()
    ]

    for index, chunk in enumerate(chunks):

        response = embeddings(
            model="nomic-embed-text",
            prompt=chunk
        )

        collection.add(
            ids=[
                f"{file.stem}_{index}"
            ],
            documents=[
                chunk
            ],
            embeddings=[
                response["embedding"]
            ]
        )

print("INDEXADO COMPLETADO")