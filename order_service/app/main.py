from fastapi import FastAPI
from app.routes import orders
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Order Service")

app.include_router(orders.router, prefix="/products")