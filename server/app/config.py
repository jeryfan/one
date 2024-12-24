from functools import lru_cache
from os import path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings as Base

__all__ = ["get_settings"]

ENV_FILES = (".env", ".env.prod")
ROOT_PATH = path.dirname(path.abspath(path.join(__file__, "..")))


class BaseSettings(Base):
    """配置基类"""

    class Config:
        env_file = ENV_FILES
        env_file_encoding = "utf-8"


class Settings(BaseSettings):
    """应用配置
    server目录为后端项目根目录, 在该目录下创建 ".env" 文件, 写入环境变量(默认大写)会自动加载, 并覆盖同名配置(小写)
        eg.
        .env 文件内写入:
            REDIS_URL='redis://localhost:6379'
            上述环境变量会覆盖 redis_url
    """

    # 数据库设置
    database_url: str = "mongodb://one:one@one-mongo:27017/one?authSource=admin"
    database_name: str = "one"

    # Celery配置
    celery_name: str = "tasks"
    celery_broker: str = "redis://:one@one-redis:6379/1"
    celery_backend: str = "redis://:one@one-redis:6379/2"

    # mysql
    # 数据库连接池最小值
    database_pool_min_size: int = 5
    # 数据库连接池最大值
    database_pool_max_size: int = 20
    # 数据库连接最大空闲时间
    database_pool_recycle: int = 300

    # redis
    redis_url: str = "redis://:one@one-redis:6379/5"


@lru_cache()
def get_settings() -> Settings:
    """获取并缓存应用配置"""
    # 读取server目录下的配置
    for f in ENV_FILES:
        load_dotenv(dotenv_path=path.join(ROOT_PATH, f))
    return Settings()


settings = get_settings()
