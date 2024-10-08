# controllers.py
from fastapi import APIRouter
from pydantic import BaseModel
from slowapi import Limiter
from slowapi.util import get_remote_address
from business import create_user
from schemas import userCreate

limiter = Limiter(key_func=get_remote_address)

router = APIRouter()

user_create = userCreate

@router.get("/")
def hello_world():
    return {"message": "Hello World"}

@router.post("/register")
def add_user(user: userCreate):
    new_user = create_user(user)
    return {"message": "Item added successfully", "item": new_user}
