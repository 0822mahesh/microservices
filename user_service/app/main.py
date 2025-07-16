from fastapi import FastAPI
from app.routes import auth
from app.core.database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Service")

# Add auth endpoints
app.include_router(auth.router, prefix="/auth")