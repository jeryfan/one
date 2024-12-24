from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ["TimestampMixin"]


class TimestampMixin(BaseModel):

    create_time: datetime = Field(default_factory=lambda: datetime.now())
    update_time: datetime = Field(default_factory=lambda: datetime.now())
