from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schema import UserCreate
from app.services.user_service import UserService
from app.core.dependencies import require_role

router = APIRouter(tags=["Users"])

user_service = UserService()

@router.post("/")
async def create_user(
    user: UserCreate,
    admin=Depends(require_role("admin"))
):
    try:
        return await user_service.create_user(user.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
async def get_users(admin=Depends(require_role("admin"))):
    return await user_service.get_all_users()
