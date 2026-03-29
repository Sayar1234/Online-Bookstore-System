from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token

user_repo = UserRepository()

class AuthService:

    async def register(self, data: dict):
        existing_user = await user_repo.get_by_email(data["email"])
        if existing_user:
            raise Exception("User already exists")

        hashed_password = hash_password(data["password"])

        user_data = {
            "email": data["email"],
            "password": hashed_password,
            "role": data.get("role", "customer")
        }

        user_id = await user_repo.create_user(user_data)
        return user_id

    async def login(self, email: str, password: str):
        user = await user_repo.get_by_email(email)

        if not user:
            raise Exception("Invalid credentials")

        if not verify_password(password, user["password"]):
            raise Exception("Invalid credentials")

        token = create_access_token({"user_id": str(user["_id"])})

        return {
            "access_token": token,
            "token_type": "bearer"
        }
