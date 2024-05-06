import json
from fastapi import APIRouter
from fastapi.responses import FileResponse

permission_router = APIRouter(
    prefix="",
    tags=["permission"],
)

@permission_router.get("/role/permissions/tree")
def get_role_permissions_tree():
    with open("./raw_data/permissions_tree.json", "r", encoding="UTF-8") as f:
        content = f.read()

    return json.loads(content)

@permission_router.get("/permission/menu/tree")
def get_permissions_menu_tree():
    with open("./raw_data/menu_tree.json", "r", encoding="UTF-8") as f:
        content = f.read()

    return json.loads(content)

@permission_router.get("/permission/tree")
def get_permissions_tree():
    with open("./raw_data/permissions_tree_all.json", "r", encoding="UTF-8") as f:
        content = f.read()

    return json.loads(content)


