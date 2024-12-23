from fastapi import APIRouter
from app.tasks.test_task import test_task

router = APIRouter(prefix="/test")


@router.get("/test")
async def test():
    task = test_task.delay()
    return {"msg": "test", "task_id": task.id}
