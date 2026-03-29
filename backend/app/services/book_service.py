from app.repositories.book_repository import BookRepository

book_repo = BookRepository()

class BookService:

    async def create_book(self, data: dict):
        book_id = await book_repo.create_book(data)
        return book_id

    async def get_books(self):
        return await book_repo.get_all()

    async def get_book(self, book_id: str):
        book = await book_repo.get_by_id(book_id)
        if not book:
            raise Exception("Book not found")

        book["_id"] = str(book["_id"])
        return book

    async def update_book(self, book_id: str, data: dict):
        await book_repo.update_book(book_id, data)

    async def delete_book(self, book_id: str):
        await book_repo.delete_book(book_id)
