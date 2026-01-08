from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class CustomerIn(BaseModel):
    name: str
    cpf: Optional[str] = None
    phone: str

class OrderItem(BaseModel):
    sku: str
    name: str
    qty: int = Field(ge=1)
    price: float = Field(ge=0)
    mods: Optional[Dict[str, Any]] = None

class OrderCreateIn(BaseModel):
    customer: CustomerIn
    items: List[OrderItem]
    delivery_address: Optional[str] = None
    notes: Optional[str] = None
