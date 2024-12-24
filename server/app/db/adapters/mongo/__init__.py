from .motor_odm import Document


from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

__all__ = ["db"]

# 数据库实例
db = AsyncIOMotorClient(settings.database_url)
Document.use(db.get_default_database(settings.database_name))
