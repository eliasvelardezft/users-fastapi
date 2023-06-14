from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .v1 import routers
from config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    openapi_url=settings.OPEN_API_URL,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["OPTIONS", "GET", "POST", "DELETE", "PUT", "PATCH"],
    allow_headers=["*"],
)

# routers
app.include_router(routers.router, prefix="/api/v1", tags=["v1"])
