import json
from fastapi import APIRouter
from fastapi.responses import FileResponse

role_router = APIRouter(
    prefix="/role",
    tags=["role"],
)

@role_router.get("")
def get_role(enable=1):
    with open("./raw_data/role_all.json", "r", encoding="UTF-8") as f:
        content = f.read()

    return json.loads(content)

@role_router.get("/page")
def get_user_detail(pageNo=1, pageSize=10, name='超级管理员'):
    with open("./raw_data/role_all.json", "r", encoding="UTF-8") as f:
        content = f.read()

    return json.loads(content)

