import time
from fastapi import Request, FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logger import log
from app.core.config import settings


class RequestTimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # 处理请求
        response = await call_next(request)
        
        # 计算处理时间
        process_time = time.time() - start_time
        
        # 记录请求信息
        log.info(
            f"Method: {request.method} Path: {request.url.path} "
            f"Status: {response.status_code} Time: {process_time:.3f}s"
        )
        
        # 添加处理时间到响应头
        response.headers["X-Process-Time"] = str(process_time)
        
        return response


def setup_middleware(app: FastAPI):
    """配置所有中间件"""
    # 添加请求计时中间件
    app.add_middleware(RequestTimingMiddleware)
    
    # 如果需要添加其他中间件，可以在这里添加
    # 例如：CORS、认证、限流等中间件 