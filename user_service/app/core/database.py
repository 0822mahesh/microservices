from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import sqlite_url

engine = create_engine(sqlite_url)
Sessionmaker = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Sessionmaker()
    try:
        yield db
    except Exception as e:
        print("Error in DB session:", e)
        raise e
    except:
        db.close()