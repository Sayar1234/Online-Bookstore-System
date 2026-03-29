def order_item_model(order_id: str, book_id: str, quantity: int, price: float):
    return {
        "order_id": order_id,
        "book_id": book_id,
        "quantity": quantity,
        "price": price
    }
