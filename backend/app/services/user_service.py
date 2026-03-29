from app.repositories.user_repository import UserRepository
from app.core.security import hash_password

user_repo = UserRepository()

class UserService:

    async def create_user(self, data: dict):
        existing = await user_repo.get_by_email(data["email"])
        if existing:
            raise Exception("User already exists")

        data["password"] = hash_password(data["password"])
        user_id = await user_repo.create_user(data)
        return user_id

    async def get_user(self, user_id: str):
        user = await user_repo.get_by_id(user_id)
        if not user:
            raise Exception("User not found")

        user["_id"] = str(user["_id"])
        return user

    async def get_all_users(self):
        return await user_repo.get_all()
