from app.db.mongo_client import get_database
from bson import ObjectId

class UserRepository:

    def __init__(self):
        pass
    
    @property
    def collection(self):
        return get_database()["users"]

    async def create_user(self, user_data: dict):
        result = await self.collection.insert_one(user_data)
        return str(result.inserted_id)

    async def get_by_email(self, email: str):
        return await self.collection.find_one({"email": email})

    async def get_by_id(self, user_id: str):
        return await self.collection.find_one({"_id": ObjectId(user_id)})

    async def get_all(self):
        users = []
        cursor = self.collection.find({})
        async for user in cursor:
            user["_id"] = str(user["_id"])
            users.append(user)
        return users
