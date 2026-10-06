from fastapi import FastAPI

app = FastAPI(title="RAG API")

@app.get("/")
def root():
    return {"service": "RAG API", "status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/search")
def search(query: str):
    # Заглушка — в реальной системе здесь поиск в Qdrant + генерация LLM
    return {
        "query": query,
        "results": [
            {"doc": "internal_policy.pdf", "score": 0.92},
            {"doc": "onboarding.docx", "score": 0.87}
        ]
    }
