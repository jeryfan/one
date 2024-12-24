from app.db.adapters.mongo import Document
from .base import TimestampMixin
from pymongo import IndexModel


class User(Document, TimestampMixin):

    class Mongo:
        collection = "users"
        indexes = [
            IndexModel("username"),
        ]

    username: str
    password: str

