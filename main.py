from fastapi import FastAPI

app = FastAPI(
    title="Exammero RAG Engine",
    version="0.0.1"
)


@app.get("/")
def root():
    return {
        "service": "Exammero RAG Engine",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }