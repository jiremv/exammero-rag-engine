from app.config import DOCUMENTS_PATH
from app.core.document_loader import load_documents
from app.core.embeddings import generate_embedding
from app.core.vector_store import collection


def build_index():

    docs = load_documents(
        DOCUMENTS_PATH
    )

    for idx, doc in enumerate(docs):

        embedding = generate_embedding(
            doc["content"]
        )

        collection.add(
            ids=[str(idx)],
            embeddings=[embedding],
            documents=[doc["content"]],
            metadatas=[
                {
                    "source": doc["file_name"]
                }
            ]
        )

    print(
        f"{len(docs)} documents indexed"
    )


if __name__ == "__main__":
    build_index()