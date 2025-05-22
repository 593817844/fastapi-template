from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.core.database import init_db, close_db
from app.core.middleware import setup_middleware
from app.core.logger import log
from app.core.redis import redis_client
from app.routers import user


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行
    await init_db()
    await redis_client.init_client()
    log.info("Application startup")
    yield
    # 关闭时执行
    await redis_client.close()
    await close_db()
    log.info("Application shutdown")


def create_app() -> FastAPI:
    """创建FastAPI应用"""
    app = FastAPI(
        title="FastAPI Template",
        description="A FastAPI template with MySQL, Redis, and logging",
        version="1.0.0",
        debug=settings.DEBUG,
        lifespan=lifespan
    )

    # 设置中间件
    setup_middleware(app)

    # 注册路由
    app.include_router(user.router)

    # 添加路由
    @app.get("/")
    async def root():
        return {"message": "Welcome to FastAPI Template"}

    return app


app = create_app() 