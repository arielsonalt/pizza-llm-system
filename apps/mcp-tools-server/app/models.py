from sqlalchemy import Column, String, DateTime, Integer, Numeric, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(String, primary_key=True)  # uuid string
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=True, index=True)
    phone = Column(String, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    orders = relationship("Order", back_populates="customer")

class Order(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True)  # uuid string
    customer_id = Column(String, ForeignKey("customers.id"), nullable=False, index=True)

    status = Column(String, nullable=False, default="created")
    total = Column(Numeric(10, 2), nullable=False, default=0)

    delivery_address = Column(String, nullable=True)
    items = Column(JSON, nullable=False)  # [{sku,name,qty,price,mods...}]
    notes = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.astimezone, nullable=False)

    customer = relationship("Customer", back_populates="orders")
