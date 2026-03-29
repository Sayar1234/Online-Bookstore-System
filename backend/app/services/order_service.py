from app.repositories.order_repository import OrderRepository
from app.repositories.order_item_repository import OrderItemRepository
from app.repositories.book_repository import BookRepository

order_repo = OrderRepository()
order_item_repo = OrderItemRepository()
book_repo = BookRepository()

class OrderService:

    async def create_order(self, user_id: str, data: dict):
        items = data["items"]

        order_items = []
        total_amount = 0

        for item in items:
            book = await book_repo.get_by_id(item["book_id"])

            if not book:
                raise Exception("Book not found")

            if book["stock"] < item["quantity"]:
                raise Exception("Insufficient stock")

            price = book["price"]
            total = price * item["quantity"]

            total_amount += total

            order_items.append({
                "book_id": item["book_id"],
                "quantity": item["quantity"],
                "price": price
            })

        order_data = {
            "user_id": user_id,
            "total_amount": total_amount,
            "status": "pending"
        }

        order_id = await order_repo.create_order(order_data)

        for item in order_items:
            item["order_id"] = order_id

        await order_item_repo.create_many(order_items)

        return order_id

    async def get_user_orders(self, user_id: str):
        return await order_repo.get_by_user(user_id)

    async def get_order_details(self, order_id: str):
        order = await order_repo.get_by_id(order_id)
        if not order:
            raise Exception("Order not found")

        order["_id"] = str(order["_id"])

        items = await order_item_repo.get_by_order_id(order_id)

        return {
            "order": order,
            "items": items
        }

    async def get_all_orders(self):
        return await order_repo.get_all()
