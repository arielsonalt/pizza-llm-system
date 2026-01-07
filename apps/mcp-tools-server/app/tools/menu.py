from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_menu():
    return {"items": ["Margherita", "Pepperoni", "Calabresa"]}
