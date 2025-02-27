
from pydantic import Field
from pydantic_settings import BaseSettings


class MongoConfig(BaseSettings):
    MONGO_DB_URL: str = Field(default=None)
    MONGO_DB_NAME: str = Field(default=None)