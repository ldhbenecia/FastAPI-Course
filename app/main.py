from fastapi import FastAPI, APIRouter

from .database import Base, engine
from .routers import user, item

Base.metadata.create_all(bind=engine)

app = FastAPI()

api_router = APIRouter()
app.include_router(user.router)
app.include_router(item.router)

app.include_router(api_router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}
