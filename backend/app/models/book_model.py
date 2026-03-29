from datetime import datetime

def book_model(data: dict):
    return {
        "title": data["title"],
        "author": data["author"],
        "price": data["price"],
        "stock": data.get("stock", 0),
        "created_at": datetime.utcnow()
    }
