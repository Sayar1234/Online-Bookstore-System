from app.repositories.cart_repository import CartRepository
from app.repositories.book_repository import BookRepository

cart_repo = CartRepository()
book_repo = BookRepository()

class CartService:

    async def get_cart(self, user_id: str):
        cart_items = await cart_repo.get_by_user(user_id)
        # populate book data in response
        populated = []
        for item in cart_items:
            book = await book_repo.get_by_id(item["book_id"])
            if book:
                populated.append({
                    "book_id": item["book_id"],
                    "title": book.get("title"),
                    "price": book.get("price"),
                    "quantity": item.get("quantity", 1),
                })
        return populated

    async def add_to_cart(self, user_id: str, book_id: str):
        book = await book_repo.get_by_id(book_id)
        if not book:
            raise Exception("Book not found")

        await cart_repo.add_or_update(user_id, book_id, quantity=1)

    async def remove_from_cart(self, user_id: str, book_id: str):
        await cart_repo.remove_item(user_id, book_id)

    async def clear_cart(self, user_id: str):
        await cart_repo.clear_cart(user_id)
