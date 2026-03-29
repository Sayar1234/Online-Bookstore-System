from app.db.mongo_client import get_database
from bson import ObjectId

class BookRepository:

    def __init__(self):
        pass
    
    @property
    def collection(self):
        return get_database()["books"]

    async def create_book(self, book_data: dict):
        result = await self.collection.insert_one(book_data)
        return str(result.inserted_id)

    async def get_by_id(self, book_id: str):
        return await self.collection.find_one({"_id": ObjectId(book_id)})

    async def get_all(self):
        books = []
        cursor = self.collection.find({})
        async for book in cursor:
            book["_id"] = str(book["_id"])
            books.append(book)
        return books

    async def update_book(self, book_id: str, update_data: dict):
        await self.collection.update_one(
            {"_id": ObjectId(book_id)},
            {"$set": update_data}
        )

    async def delete_book(self, book_id: str):
        await self.collection.delete_one({"_id": ObjectId(book_id)})
