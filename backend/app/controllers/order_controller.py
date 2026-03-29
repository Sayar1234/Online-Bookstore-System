from fastapi import APIRouter, HTTPException, Depends
from app.schemas.order_schema import OrderCreate
from app.services.order_service import OrderService
from app.core.dependencies import get_current_user

router = APIRouter(tags=["Orders"])

order_service = OrderService()

@router.post("/")
async def place_order(order: OrderCreate, user=Depends(get_current_user)):
    try:
        order_id = await order_service.create_order(str(user["_id"]), order.dict())
        return {"order_id": order_id}
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
