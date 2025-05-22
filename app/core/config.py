from typing import Optional
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    # App settings
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DEBUG: bool = True
    
    # Server settings
    WORKERS_COUNT: int = 4  # 工作进程数
    WORKER_CONNECTIONS: int = 1000  # 每个工作进程的最大并发连接数
    KEEPALIVE: int = 5  # keepalive 超时时间（秒）

    # Database settings
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    # Redis settings
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    REDIS_PASSWORD: Optional[str] = None

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def REDIS_URL(self) -> str:
        if self.REDIS_PASSWORD:
            return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    class Config:
        env_file = ".env"
        case_sensitive = True
        env_file_encoding = 'utf-8'
        # 设置环境变量优先级高于配置文件
        env_nested_delimiter = '__'
        # 允许从环境变量覆盖所有配置
        extra = 'allow'


settings = Settings() 