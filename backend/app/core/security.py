from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hash_password: str):
    return pwd_context.verify(password, hash_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expire": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm = settings.JWT_ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])