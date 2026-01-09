import os
import requests
from fastapi import APIRouter

router = APIRouter()
AGENT_URL = os.getenv("AGENT_ORCHESTRATOR_URL", "http://agent-orchestrator:8000")

@router.post("/chat")
def chat(payload: dict):
    r = requests.post(f"{AGENT_URL}/chat", json=payload, timeout=60)
    print(requests)
    r.raise_for_status()
    return r.json()
