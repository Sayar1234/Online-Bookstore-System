import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.mongo_client import connect_to_mongo, close_mongo_connection, get_database
from app.models.user_model import user_model
from app.core.security import hash_password
from app.core.config import settings


async def create_admin_user():
    try:
        await connect_to_mongo()

        db = get_database()
        users_collection = db["users"]

        existing_admin = await users_collection.find_one({"role": "admin"})
        if existing_admin:
            print("✓ Admin user already exists!")
            return

        admin_data = {
            "email": settings.ADMIN_EMAIL,
            "password": settings.ADMIN_PASSWORD,
            "role": "admin"
        }

        user_doc = user_model(admin_data)
        password_to_hash = user_doc["password"][:72] if len(user_doc["password"]) > 72 else user_doc["password"]
        user_doc["password"] = hash_password(password_to_hash)

        result = await users_collection.insert_one(user_doc)
        print("✓ Admin user created successfully!")
        print(f"  Email: {admin_data['email']}")
        print(f"  Password: {admin_data['password']}")
        print(f"  Role: {admin_data['role']}")
        print(f"  User ID: {result.inserted_id}")

    except Exception as e:
        print(f"✗ Error creating admin user: {str(e)}")
        sys.exit(1)
    finally:
        await close_mongo_connection()


if __name__ == "__main__":
    print("Creating admin user...")
    asyncio.run(create_admin_user())
    print("Done!")