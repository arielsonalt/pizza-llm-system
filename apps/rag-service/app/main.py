from fastapi import FastAPI
from app.retrieval.query import query_index

app = FastAPI(title="RAG Service")

@app.post("/rag/query")
def query(payload: dict):
    return query_index(payload["query"])
