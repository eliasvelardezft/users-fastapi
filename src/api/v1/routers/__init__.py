from fastapi import APIRouter

from .user import router as users_router
from .role import router as roles_router


router = APIRouter()


router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(roles_router, prefix="/roles", tags=["roles"])
