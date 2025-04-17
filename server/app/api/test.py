from fastapi import APIRouter


router = APIRouter(prefix="/test")


@router.get("/test")
async def test():
    return {"msg": "test"}
