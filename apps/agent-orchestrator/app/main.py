from fastapi import FastAPI
from app.graph.flow import graph

app = FastAPI(title="Agent Orchestrator")

@app.post("/agent/chat")
async def chat(payload: dict):
    result = await graph.ainvoke(payload)
    return result
