from fastapi import FastAPI

from router.data_router import data_router
from router.auth_router import auth_router
from router.user_router import user_router
from router.role_router import role_router
from router.permission_router import permission_router

description = """
this is backend for libcity 3D
"""

app = FastAPI(title="libcity3D", version="0.1.0", description=description)
# api_app = FastAPI(title="libcity3D API")
# api_app.include_router(data_router)
# app.mount("/api", api_app)
app.include_router(data_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(permission_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
