from fastapi import APIRouter

"""
用于和libcity进行交互
"""

model_router = APIRouter(
    prefix="/model",
    tags=["model"],
)
