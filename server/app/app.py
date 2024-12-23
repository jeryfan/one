from fastapi import FastAPI


def config_api_router(app: FastAPI, prefix: str = "/api"):
    from app.api import test

    app.include_router(test.router, prefix=prefix)


def create_app() -> FastAPI:
    app = FastAPI()
    config_api_router(app)
    return app
