from datetime import datetime

def user_model(data: dict):
    return {
        "email": data["email"],
        "password": data["password"],
        "role": data.get("role", "customer"),
        "created_at": datetime.utcnow()
    }
