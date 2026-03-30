from app.db.mongo_client import get_database
from bson import ObjectId

class CartRepository:

    def __init__(self):
        pass

    @property
    def collection(self):
        return get_database()["cart"]

    async def get_by_user(self, user_id: str):
        items = []
        cursor = self.collection.find({"user_id": user_id})
        async for item in cursor:
            item["_id"] = str(item["_id"])
            items.append(item)
        return items

    async def get_item(self, user_id: str, book_id: str):
        return await self.collection.find_one({"user_id": user_id, "book_id": book_id})

    async def add_or_update(self, user_id: str, book_id: str, quantity: int = 1):
        existing = await self.get_item(user_id, book_id)
        if existing:
            await self.collection.update_one(
                {"_id": ObjectId(existing["_id"])},
                {"$set": {"quantity": existing["quantity"] + quantity}}
            )
            return

        cart_item = {
            "user_id": user_id,
            "book_id": book_id,
            "quantity": quantity
        }
        await self.collection.insert_one(cart_item)

    async def remove_item(self, user_id: str, book_id: str):
        await self.collection.delete_one({"user_id": user_id, "book_id": book_id})

    async def clear_cart(self, user_id: str):
        await self.collection.delete_many({"user_id": user_id})
