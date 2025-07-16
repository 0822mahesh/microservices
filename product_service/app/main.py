from fastapi import FastAPI
from app.routes import products
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Service")

app.include_router(products.router, prefix="/products")