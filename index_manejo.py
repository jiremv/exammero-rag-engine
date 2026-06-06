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

    response = embeddings(
        model="nomic-embed-text",
        prompt=content
    )

    collection.add(
        ids=[file.name],
        documents=[content],
        embeddings=[response["embedding"]]
    )

print("INDEXADO COMPLETADO")