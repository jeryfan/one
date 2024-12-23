from app.celery_app import celery_app


@celery_app.task
def test_task():
    print("test_task")
    return "test_task"
