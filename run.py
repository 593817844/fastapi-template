import uvicorn
import sys
from app.core.config import settings
from app.core.logger import log


def start_server():
    """启动服务器"""
    log.info("Starting FastAPI application...")
    
    if settings.DEBUG:
        # 开发环境：使用 uvicorn 直接运行
        uvicorn.run(
            "app.main:app",
            host=settings.APP_HOST,
            port=settings.APP_PORT,
            reload=True,
            log_level="debug"
        )
    else:
        # 生产环境：使用 uvicorn 的 Gunicorn 集成
        uvicorn.run(
            "app.main:app",
            host=settings.APP_HOST,
            port=settings.APP_PORT,
            workers=settings.WORKERS_COUNT,
            loop="uvloop" if sys.platform != "win32" else "auto",  # 在非Windows系统上使用uvloop
            http="httptools",  # 使用 httptools 提高性能
            limit_concurrency=settings.WORKER_CONNECTIONS,
            timeout_keep_alive=settings.KEEPALIVE,
            log_level="info",
            access_log=True,
            use_colors=False,  # 生产环境禁用颜色输出
            proxy_headers=True,  # 支持代理头
            forwarded_allow_ips="*"  # 允许所有代理IP
        )


if __name__ == "__main__":
    start_server() 