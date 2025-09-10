from fastapi import APIRouter, Depends
from app.api.deps import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
async def get_me(current_user: dict = Depends(get_current_user)):
    return {"user": current_user}
