from fastapi import FastAPI
from pydantic import BaseModel
from app.llm import get_llm

app = FastAPI(title="Agent Orchestrator")

class ChatIn(BaseModel):
    message: str

@app.post("/chat")
def chat(payload: ChatIn):
    llm = get_llm()
    resp = llm.invoke(payload.message)
    return {"reply": resp.content}
