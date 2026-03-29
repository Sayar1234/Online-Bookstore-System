from app.db.mongo_client import get_database
from bson import ObjectId

class OrderRepository:

    def __init__(self):
        pass
    
    @property
    def collection(self):
        return get_database()["orders"]

    async def create_order(self, order_data: dict):
        result = await self.collection.insert_one(order_data)
        return str(result.inserted_id)

    async def get_by_id(self, order_id: str):
        return await self.collection.find_one({"_id": ObjectId(order_id)})

    async def get_by_user(self, user_id: str):
        orders = []
        cursor = self.collection.find({"user_id": user_id})
        async for order in cursor:
            order["_id"] = str(order["_id"])
            orders.append(order)
        return orders

    async def get_all(self):
        orders = []
        cursor = self.collection.find({})
        async for order in cursor:
            order["_id"] = str(order["_id"])
            orders.append(order)
        return orders
