from app.celery_app import celery_app
import time


@celery_app.task
def test_task():
    timestamp = time.time()
    print("test_schedule_task", timestamp)
    return timestamp
