from fastapi import FastAPI

from app.api.rag_controller import router as rag_router

app = FastAPI(
    title="Exammero RAG Engine",
    version="0.0.1"
)

app.include_router(rag_router)


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