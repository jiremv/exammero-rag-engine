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
            n_results=5
        )

        print(
            result["documents"][0]
        )
        
        return "\n\n".join(
            result["documents"][0]
        )        