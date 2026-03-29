from fastapi import APIRouter, HTTPException, Depends
from app.schemas.auth_schema import RegisterSchema, LoginSchema, TokenResponse
from app.services.auth_service import AuthService
from app.core.dependencies import get_current_user

router = APIRouter(tags=["Auth"])

auth_service = AuthService()

@router.post("/register", response_model=str)
async def register(user: RegisterSchema):
    try:
        return await auth_service.register(user.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
async def login(user: LoginSchema):
    try:
        return await auth_service.login(user.email, user.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.get("/me")
async def me(user=Depends(get_current_user)):
    user["_id"] = str(user["_id"])
    return user
