

from fastapi import APIRouter, HTTPException,Body
from app.models.mongo.user import User
from app.utils.tools import ToolsUtil


router = APIRouter(prefix="/user")


@router.post("/")
async def create(username:str=Body(),password:str=Body()):
    user = await User.find_one({"username":username})
    if user:
        raise HTTPException(status_code=400,detail="用户已存在")
    hashed_password = ToolsUtil.hash(password)
    user = User(username=username,password=hashed_password)
    await user.save()
    return str(user.id)