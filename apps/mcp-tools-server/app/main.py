from fastapi import FastAPI
from app.tools import menu, orders

app = FastAPI(title="MCP Tools Server")

app.include_router(menu.router, prefix="/menu")
app.include_router(orders.router, prefix="/orders")
