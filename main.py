from fastapi import FastAPI

from router import data_router

description = """
this is backend for libcity 3D
"""

app = FastAPI(title="libcity3D", version="0.1.0", description=description)
api_app = FastAPI(title="libcity3D API")
api_app.include_router(data_router)
app.mount("/api", api_app)

@app.get("/")
def read_root():
    return {"Hello": "World"}
