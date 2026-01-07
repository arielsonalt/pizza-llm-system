import httpx

class MCPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def call(self, tool: str, payload: dict):
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{self.base_url}/{tool}", json=payload)
            return r.json()
