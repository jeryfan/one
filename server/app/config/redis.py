from pydantic import Field
from pydantic_settings import BaseSettings



class RedisConfig(BaseSettings):

    REDIS_HOST:str = Field(default="localhost")
    REDIS_PORT:str = Field(default=6379)
    REDIS_USERNAME:str = Field(default=None)
    REDIS_PASSWORD:str = Field(default=None)
    REDIS_DB:int = Field(default = 0)

    def get_redis_url(self, db: int = 0) -> str:
        auth_part = (
            f"{self.REDIS_USERNAME}:{self.REDIS_PASSWORD}@"
            if self.REDIS_USERNAME and self.REDIS_PASSWORD
            else f":{self.REDIS_PASSWORD}@" if self.REDIS_PASSWORD
            else ""
        )
        return f"redis://{auth_part}{self.REDIS_HOST}:{self.REDIS_PORT}/{db if db else self.REDIS_DB}"
    