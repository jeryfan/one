from .user import User


async def init_indexes():
    await User.init_indexes()
