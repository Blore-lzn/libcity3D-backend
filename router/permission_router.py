import json
from fastapi import APIRouter
from fastapi.responses import FileResponse

permission_router = APIRouter(
    prefix="",
    tags=["permission"],
)

@permission_router.get("/permissions/tree")
def get_permissions_tree():
    with open("./raw_data/permissions_tree.json", "r") as f:
        content = f.read()

    return json.loads(content)

@permission_router.get("/permissions/menu/tree")
def get_permissions_menu_tree():
    with open("./raw_data/menu_tree.json", "r") as f:
        content = f.read()

    return json.loads(content)

@permission_router.get("/permissions/tree")
def get_permissions_tree():
    with open("./raw_data/permissions_tree.json", "r") as f:
        content = f.read()

    return json.loads(content)


