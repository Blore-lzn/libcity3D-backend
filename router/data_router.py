from fastapi import APIRouter
import json

data_router = APIRouter(
    prefix="/data",
    tags=["data"],
)


@data_router.get("/all")
def read_models():
    return {"models": ["default"]}


@data_router.get("/test_traj")
def read_test_traj():
    with open("./raw_data/traj_1000.json", "r") as f:
        content = f.read()

    return json.loads(content)


@data_router.get("/test_state")
def read_test_state():
    with open("./raw_data/state_100081_1000.json", "r") as f:
        content = f.read()

    return json.loads(content)
