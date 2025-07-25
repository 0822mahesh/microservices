from sqlalchemy import Column, Integer,String
from app.core.database import get_db,Base

class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True, index = True)
    username = Column(String, unique=True, index=True)
    email = Column(String,index=True)
    hased_password = Column(String)