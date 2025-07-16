from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.order import Order
from pydantic import BaseModel
from typing import List
from app.core.security import verify_token

router = APIRouter()

class OrderCreate(BaseModel):
    item_name: str
    quantity: int
    total_price: float

class OrderOut(OrderCreate):
    id: int

    class Config:
        orm_mode = True

@router.post("/", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db),current_user:str=Depends(verify_token)):
    new_order = Order(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/", response_model=List[OrderOut])
def list_orders(db: Session = Depends(get_db),current_user:str=Depends(verify_token)):
    return db.query(Order).all()