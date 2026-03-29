from fastapi import APIRouter, Depends
from app.services.order_service import OrderService
from app.core.dependencies import require_role

router = APIRouter(tags=["Admin"])

order_service = OrderService()

@router.get("/orders")
async def all_orders(admin=Depends(require_role("admin"))):
    return await order_service.get_all_orders()


@router.get("/sales")
async def sales(admin=Depends(require_role("admin"))):
    orders = await order_service.get_all_orders()

    total_revenue = sum(order["total_amount"] for order in orders)

    return {
        "total_orders": len(orders),
        "total_revenue": total_revenue
    }
