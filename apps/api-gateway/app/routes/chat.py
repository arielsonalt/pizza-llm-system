from fastapi import APIRouter
from httpx import AsyncClient

router = APIRouter()

@router.post("/")
async def chat(payload: dict):
    async with AsyncClient() as client:
        resp = await client.post(
            "http://agent-orchestrator:8000/agent/chat",
            json=payload,
            timeout=30
        )
        return resp.json()
