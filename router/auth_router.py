from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import FileResponse

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


class LoginBody(BaseModel):
    username: str
    password: str
    captcha: str


@auth_router.post("/login")
def login():
    result = {
        "code": 0,
        "message": "OK",
        "data": {"accessToken": "access-token:admin:super-admin"},
        "originUrl": "/auth/login",
    }
    return result


@auth_router.get("/captcha")
def captcha():
    return FileResponse("./raw_data/captcha.svg")


@auth_router.post("/logout")
def login(): 
    result = {"code": 0, "message": "OK", "data": True, "originUrl": "/auth/logout"}
    return result


@auth_router.post("/current-role/switch/{roleCode}")
def switch_role(roleCode):
    result = {
        "code": 0,
        "message": "OK",
        "data": {"accessToken": f"access-token:admin:{roleCode}"},
        "originUrl": "/auth/current-role/switch/ROLE_QA",
    }
    return result
