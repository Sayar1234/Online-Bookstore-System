from fastapi import APIRouter, HTTPException, Depends
from app.schemas.order_schema import OrderCreate
from app.services.order_service import OrderService
from app.services.cart_service import CartService
from app.core.dependencies import get_current_user

router = APIRouter(tags=["Orders"])

order_service = OrderService()
cart_service = CartService()

@router.post("/")
async def place_order(order: OrderCreate | None = None, user=Depends(get_current_user)):
    user_id = str(user["_id"])
    try:
        if order is None:
            cart_items = await cart_service.get_cart(user_id)
            if not cart_items:
                raise HTTPException(status_code=400, detail="Cart is empty")
            items_payload = [{"book_id": item["book_id"], "quantity": item.get("quantity", 1)} for item in cart_items]
        else:
            items_payload = order.dict().get("items", [])

        order_id = await order_service.create_order(user_id, items_payload)
        await cart_service.clear_cart(user_id)
        return {"order_id": order_id}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
async def my_orders(user=Depends(get_current_user)):
    return await order_service.get_user_orders(str(user["_id"]))


@router.get("/{order_id}")
async def order_details(order_id: str, user=Depends(get_current_user)):
    try:
        return await order_service.get_order_details(order_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/cart")
async def get_cart(user=Depends(get_current_user)):
    return await cart_service.get_cart(str(user["_id"]))


@router.post("/cart/{book_id}")
async def add_to_cart(book_id: str, user=Depends(get_current_user)):
    try:
        await cart_service.add_to_cart(str(user["_id"]), book_id)
        return {"message": "Added to cart"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/cart/{book_id}")
async def remove_from_cart(book_id: str, user=Depends(get_current_user)):
    try:
        await cart_service.remove_from_cart(str(user["_id"]), book_id)
        return {"message": "Removed from cart"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
