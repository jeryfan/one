from celery import Celery
from app.config import settings
from celery.schedules import crontab
from datetime import timedelta


# 创建Celery应用程序对象
celery_app = Celery(
    settings.celery_name, broker=settings.celery_broker, backend=settings.celery_backend
)

# 配置Celery应用程序
celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    task_track_started=True,
    task_ignore_result=False,  # True
)

# 注册周期性任务的调度
celery_app.conf.beat_schedule = {
    "charge_task": {
        "task": "app.tasks.test_schedule_task.test_task",
        "schedule": crontab(minute="*/5"),
    }
}

# 导入任务模块
celery_app.autodiscover_tasks(
    [
        "app.tasks.test_task",
    ]
)
