from fastapi import APIRouter, Body
from app.models.mongo.user import User
from bson import ObjectId

router = APIRouter(prefix="/user")


@router.post("/register")
async def register(username: str = Body(), password: str = Body()):

    assert username and password
    user = User(username=username, password=password, _id=ObjectId())
    print(user)
    await user.insert()
    return str(user.id)
