import os
from dotenv import load_dotenv

load_dotenv

sqlite_file_name = "database.db"
sqlite_url = "sqlite:///./user.db"

ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 30
SECREAT_KEY = os.getenv("SECRET_KEY")
