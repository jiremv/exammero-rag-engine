from pathlib import Path


def load_documents(path: str):
    documents = []

    for file in Path(path).glob("*.txt"):
        content = file.read_text(encoding="utf-8")

        documents.append(
            {
                "file_name": file.name,
                "content": content
            }
        )

    return documents