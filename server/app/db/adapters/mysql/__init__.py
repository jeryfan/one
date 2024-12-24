from databases import Database

from app.config import settings

__all__ = ["db"]

# 数据库实例
db: Database = Database(
    settings.database_url,
    min_size=settings.database_pool_min_size,
    max_size=settings.database_pool_max_size,
    pool_recycle=settings.database_pool_recycle,
)
