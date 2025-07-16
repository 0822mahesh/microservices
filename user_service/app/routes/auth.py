from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr,Field
from app.core.database import get_db
from app.core.security import hash_password,verify_password,create_acess_token
from app.models.user import User

router = APIRouter()

class UserRegister(BaseModel):
    username:str
    email:EmailStr = Field(EmailStr)
    password:str

class UserLogin(BaseModel):
    username:str
    password:str

def create_user_from_schema(user:UserRegister)->User:
    return User(
        username = user.username,
        email=user.email,
        hased_password= hash_password(user.password)
    )
@router.post("/register")
async def register(user:UserRegister,db:Session=Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400,detail="Username already existed")
    
    new_user = create_user_from_schema(user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"User Created","username":user.username}

@router.post("/login")
async def login(user:UserLogin,db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password,db_user.hased_password):
        raise HTTPException(status_code=401,detail="Invalid Credentials")
    token = create_acess_token(data={"sub": db_user.username})
    return {"access_token":token,"token_type":"bearer"}