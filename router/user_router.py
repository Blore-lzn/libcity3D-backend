import json
from fastapi import APIRouter
from fastapi.responses import FileResponse

user_router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@user_router.get("")
def get_users(pageNo=1, pageSize=10):
    with open("./raw_data/user_all.json", "r", encoding="UTF-8") as f:
        content = f.read()

    return json.loads(content)

@user_router.get("/detail")
def get_user_detail():
    with open("./raw_data/user_detail.json", "r", encoding="UTF-8") as f:
        content = f.read()

    return json.loads(content)
