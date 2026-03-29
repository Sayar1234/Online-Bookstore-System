from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    stock: Optional[int] = 0

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    price: Optional[float]
    stock: Optional[int]

class BookResponse(BaseModel):
    id: str
    title: str
    author: str
    price: float
    stock: int
    created_at: datetime
