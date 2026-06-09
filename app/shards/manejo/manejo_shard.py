import random
import chromadb

from ollama import embeddings


class ManejoShard:

    def __init__(self):

        client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = client.get_collection(
            "manejo"
        )

    def search(
        self,
        query: str
    ):

        response = embeddings(
            model="nomic-embed-text",
            prompt=query
        )

        result = self.collection.query(
            query_embeddings=[
                response["embedding"]
            ],
            n_results=1
        )

        print(
            result["documents"][0]
        )

        return "\n\n".join(
            result["documents"][0]
        )

    def search_one(
        self,
        query: str
    ):

        response = embeddings(
            model="nomic-embed-text",
            prompt=query
        )

        result = self.collection.query(
            query_embeddings=[
                response["embedding"]
            ],
            n_results=1
        )

        return result["documents"][0][0]

    def search_random(
        self
    ):

        data = self.collection.get()

        documents = data["documents"]

        fragmento = random.choice(
            documents
        )

        print(
            f"FRAGMENTO RANDOM: {fragmento}"
        )

        return fragmento

    def get_random_fragments(
        self,
        cantidad: int = 10
    ):

        data = self.collection.get()

        documentos = data["documents"]

        return random.sample(
            documentos,
            min(
                cantidad,
                len(documentos)
            )
        )        