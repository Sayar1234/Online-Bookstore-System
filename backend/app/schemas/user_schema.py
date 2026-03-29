from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Optional[str] = "customer"

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    role: str
    created_at: datetime
