from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import api_router
from app.core.config import settings
from app.db.mongo_client import connect_to_mongo, close_mongo_connection, get_database
from app.exceptions.exception_handlers import (
    not_found_exception_handler,
    bad_request_exception_handler,
    unauthorized_exception_handler,
    forbidden_exception_handler,
    validation_exception_handler
)
from app.exceptions.custom_exceptions import (
    NotFoundException,
    BadRequestException,
    UnauthorizedException,
    ForbiddenException
)
from app.models.user_model import user_model
from app.models.book_model import book_model
from app.core.security import hash_password


async def seed_initial_data():
    """Seed initial data on startup if database is empty."""
    try:
        db = get_database()

        users_collection = db["users"]
        existing_admin = await users_collection.find_one({"role": "admin"})
        if not existing_admin:
            admin_data = {
                "email": settings.ADMIN_EMAIL,
                "password": settings.ADMIN_PASSWORD,
                "role": "admin"
            }
            admin_doc = user_model(admin_data)
            password_to_hash = admin_doc["password"][:72] if len(admin_doc["password"]) > 72 else admin_doc["password"]
            admin_doc["password"] = hash_password(password_to_hash)
            await users_collection.insert_one(admin_doc)
            print("✓ Admin user created")

        books_collection = db["books"]
        existing_books_count = await books_collection.count_documents({})

    except Exception as e:
        print(f"Warning: Could not seed initial data: {str(e)}")


app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(BadRequestException, bad_request_exception_handler)
app.add_exception_handler(UnauthorizedException, unauthorized_exception_handler)
app.add_exception_handler(ForbiddenException, forbidden_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()
    await seed_initial_data()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Online Bookstore API is running"}
