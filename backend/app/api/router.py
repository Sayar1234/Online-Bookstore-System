from fastapi import APIRouter

from app.api.routes.auth import auth_router
from app.api.routes.users import users_router
from app.api.routes.books import books_router
from app.api.routes.orders import orders_router
from app.api.routes.admin import admin_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(books_router, prefix="/books", tags=["Books"])
api_router.include_router(orders_router, prefix="/orders", tags=["Orders"])
api_router.include_router(admin_router, prefix="/admin", tags=["Admin"])
