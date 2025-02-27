


from pydantic import Field
from pydantic_settings import BaseSettings


class CeleryConfig(BaseSettings):
    # Celery配置
    CELERY_NAME: str = Field()
    CELERY_BROKER_URL: str = Field()
    CELERY_BACKEND: str =Field()