from fastapi import APIRouter

model_router = APIRouter(
    prefix="/model",
    tags=["model"],
)

@model_router.get("/all")
def read_models():
    return {"models": ["default"]}