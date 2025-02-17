from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.models.mongo.init_indexes import init_indexes


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 应用启动时的初始化逻辑
    print("start")
    # await init_indexes()
    yield
    # 应用关闭时的清理逻辑
    print("Application shutdown...")


def config_api_router(app: FastAPI, prefix: str = "/api"):
    from app.api import test, user,auth
    from app.api.llm import google
    from app.api import auth

    app.include_router(auth.router, prefix=prefix)
    app.include_router(test.router, prefix=prefix)
    app.include_router(user.router, prefix=prefix)
    app.include_router(google.router, prefix=prefix)


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    config_api_router(app)
    return app
