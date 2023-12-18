from fastapi import APIRouter

from .user import router as users_router
from .role import router as roles_router
# from .auth import router as auth_router
from .permission import router as permissions_router


router = APIRouter()


router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(roles_router, prefix="/roles", tags=["roles"])
router.include_router(permissions_router, prefix="/permissions", tags=["permissions"])
# router.include_router(auth_router, prefix="/auth", tags=["auth"])
