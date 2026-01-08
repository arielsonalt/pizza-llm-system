from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.tools import menu, orders
from app.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown 

app = FastAPI(
    title="MCP Tools Server",
    lifespan=lifespan
)

app.include_router(menu.router, prefix="/menu")
app.include_router(orders.router, prefix="/orders")
