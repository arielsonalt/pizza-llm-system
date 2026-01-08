from fastapi import APIRouter
from uuid import uuid4
from decimal import Decimal
from app.db import SessionLocal
from app.models import Customer, Order
from app.schemas import OrderCreateIn

router = APIRouter()

@router.post("/")
def create_order(payload: OrderCreateIn):
    db = SessionLocal()
    try:
        # upsert customer by phone
        cust = db.query(Customer).filter(Customer.phone == payload.customer.phone).first()
        if not cust:
            cust = Customer(
                id=str(uuid4()),
                name=payload.customer.name,
                cpf=payload.customer.cpf,
                phone=payload.customer.phone,
            )
            db.add(cust)
            db.flush()
        else:
            # update basic fields if provided
            cust.name = payload.customer.name or cust.name
            cust.cpf = payload.customer.cpf or cust.cpf

        total = sum(Decimal(str(i.price)) * i.qty for i in payload.items)

        order = Order(
            id=str(uuid4()),
            customer_id=cust.id,
            status="created",
            total=total,
            delivery_address=payload.delivery_address,
            items=[i.model_dump() for i in payload.items],
            notes=payload.notes,
        )
        db.add(order)
        db.commit()

        return {"order_id": order.id, "status": order.status, "total": float(order.total)}
    finally:
        db.close()
