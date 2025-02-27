

from pydantic import Field
from pydantic_settings import BaseSettings


class AuthConfig(BaseSettings):
    
    SECRET_KEY:str = Field(default=None)
    
    GOOGLE_API_KEY:str = Field(default=None)
    GOOGLE_BASE_URL:str = Field(default=None)