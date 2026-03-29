from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.schemas.order_item_schema import OrderItemCreate

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

class OrderResponse(BaseModel):
    id: str
    user_id: str
    total_amount: float
    status: str
    created_at: datetime
