
from pydantic_settings import SettingsConfigDict
from app.config.redis import RedisConfig
from app.config.mongo import MongoConfig
from app.config.celery import CeleryConfig
from app.config.auth import AuthConfig


class OneConfig(RedisConfig,MongoConfig,CeleryConfig,AuthConfig):
    

    model_config = SettingsConfigDict(
        # read from dotenv format config file
        env_file=".env",
        env_file_encoding="utf-8",
        # ignore extra attributes
        extra="ignore",
    )




settings = OneConfig()
print(settings.model_dump())