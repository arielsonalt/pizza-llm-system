from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_order(order: dict):
    return {"order_id": "ORD123", "status": "created"}
