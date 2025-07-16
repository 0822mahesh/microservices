from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError,jwt
from app.core.config import ACESS_TOKEN_EXPIRE_MINUTES,ALGORITHM,SECREAT_KEY
import os

pwd_contxt = CryptContext(schemes=["bcrypt"], deprecated ="auto")

def hash_password(password:str) -> str:
    return pwd_contxt.hash(password)

def verify_password(password:str,hased_password:str) -> bool:
    return pwd_contxt.verify(password,hased_password)

def create_acess_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    print(os.getenv("SECRET_KEY"))
    print("********************************")
    print(type(os.getenv("SECRET_KEY")))
    return jwt.encode(to_encode,os.getenv("SECREAT_KEY"),algorithm=ALGORITHM)



