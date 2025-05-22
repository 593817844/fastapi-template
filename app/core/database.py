from tortoise import Tortoise
from app.core.config import settings
from app.core.logger import log
from app.models.user import User  # 导入 User 模型


async def init_db():
    """初始化数据库连接"""
    try:
        await Tortoise.init(
            db_url=settings.DATABASE_URL,
            modules={'models': ['app.models.user']}  # 注册 User 模型
        )
        log.info("Database connection established")
    except Exception as e:
        log.error(f"Database connection failed: {e}")
        raise


async def close_db():
    """关闭数据库连接"""
    await Tortoise.close_connections()
    log.info("Database connections closed") 