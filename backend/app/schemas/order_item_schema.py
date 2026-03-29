from pydantic import BaseModel

class OrderItemCreate(BaseModel):
    book_id: str
    quantity: int

class OrderItemResponse(BaseModel):
    book_id: str
    quantity: int
    price: float
