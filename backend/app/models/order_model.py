from datetime import datetime

def order_model(user_id: str, total_amount: float):
    return {
        "user_id": user_id,
        "total_amount": total_amount,
        "status": "pending",
        "created_at": datetime.utcnow()
    }
