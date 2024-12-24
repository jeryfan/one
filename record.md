### celery beat 数据存储

默认 celery beat 任务使用默认 SQLite 作为调度器存储，缺点是会在当前目录生成.db 文件

#### 使用 redbeat

```python
beat_scheduler="redbeat.RedBeatScheduler",  # 使用 RedBeat 作为调度器
redbeat_redis_url=settings.celery_broker,  # RedBeat 使用的 Redis 数据库
redbeat_lock_timeout=600,  # 调度任务锁超时时间（秒）
```

redbeat 的源码托管在 GitHub

```bash
poetry add git+https://github.com/sibson/redbeat.git
或者
pip install git+https://github.com/sibson/redbeat.git
```
