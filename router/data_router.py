from fastapi import APIRouter
import json

data_router = APIRouter(
    prefix="/data",
    tags=["data"],
)


@data_router.get("")
def read_datas(pageNo=1, pageSize=10):
    with open("./raw_data/data_all.json", "r", encoding="UTF-8") as f:
        content = f.read()
    return json.loads(content)


@data_router.get("/test_traj")
def read_test_traj():
    with open("./raw_data/traj_1000.json", "r") as f:
        content = f.read()

    return {
        "code": 0,
        "message": "OK",
        "data": json.loads(content),
        "originUrl": "/role?enable=1"
    }


@data_router.get("/test_state")
def read_test_state():
    with open("./raw_data/state_100081_1000.json", "r") as f:
        content = f.read()

    return json.loads(content)
