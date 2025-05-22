import aioredis
from app.core.config import settings
from app.core.logger import log


class RedisClient:
    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def init_client(self):
        """初始化Redis客户端"""
        if self._client is None:
            try:
                self._client = await aioredis.from_url(
                    settings.REDIS_URL,
                    encoding="utf-8",
                    decode_responses=True
                )
                # 测试连接
                await self._client.ping()
                log.info("Redis connection established")
            except Exception as e:
                log.error(f"Redis connection failed: {e}")
                raise

    async def get_client(self):
        """获取Redis客户端实例"""
        if self._client is None:
            await self.init_client()
        return self._client

    async def close(self):
        """关闭Redis连接"""
        if self._client is not None:
            await self._client.close()
            self._client = None
            log.info("Redis connection closed")


# 创建全局Redis客户端实例
redis_client = RedisClient() 