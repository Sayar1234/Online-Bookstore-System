from app.db.mongo_client import get_database

class OrderItemRepository:

    def __init__(self):
        pass
    
    @property
    def collection(self):
        return get_database()["order_items"]

    async def create_many(self, items: list):
        if items:
            result = await self.collection.insert_many(items)
            return [str(id) for id in result.inserted_ids]
        return []

    async def get_by_order_id(self, order_id: str):
        items = []
        cursor = self.collection.find({"order_id": order_id})
        async for item in cursor:
            item["_id"] = str(item["_id"])
            items.append(item)
        return items
