from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.product import Product
from pydantic import BaseModel
from typing import List
from app.core.security import verify_token

router = APIRouter()

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class ProductOut(ProductCreate):
    id: int

    class Config:
        orm_mode = True

@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db),current_user:str=Depends(verify_token)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/", response_model=List[ProductOut])
def list_products(db: Session = Depends(get_db),current_user:str=Depends(verify_token)):
    return db.query(Product).all()