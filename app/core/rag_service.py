from app.core.embeddings import generate_embedding
from app.core.vector_store import collection


def query_documents(question: str, top_k: int = 3):

    embedding = generate_embedding(question)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return results