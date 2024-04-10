import json
from fastapi import APIRouter
from fastapi.responses import FileResponse

role_router = APIRouter(
    prefix="",
    tags=["role"],
)


