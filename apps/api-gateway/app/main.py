from fastapi import FastAPI
from app.routes import health, chat

app = FastAPI(title="Pizza API Gateway")

app.include_router(health.router, prefix="")
app.include_router(chat.router, prefix="")

@app.get("/")
def root():
    return {"service": "api-gateway", "status": "ok"}
