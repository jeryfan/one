from app.celery_app import celery_app
from celery import Task




class BaseTask(Task):
    
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        return super().on_failure(exc, task_id, args, kwargs, einfo)
    
    def on_success(self, retval, task_id, args, kwargs):
        print("success")
        return super().on_success(retval, task_id, args, kwargs)


@celery_app.task(bind=True,base=BaseTask)
def worker(self,task):
    task_id = self.request.id
    print(task_id,task)


class TaskManager:
    
    def __init__(self):
        pass
    
    def enqueue_task(self,task):
        return worker.delay(task)
    
        
    def train_file(self):
        
        task = {}
        task_id = self.enqueue_task(task)
        
        
    def train_kb_file(self):
        pass
    
    
    def cencel_file_task(task_id):
        worker.invoke(task_id)