import sys
import os
from loguru import logger
from pathlib import Path

# 创建日志目录
log_path = Path("logs")
if not log_path.exists():
    log_path.mkdir(parents=True)

# 获取环境变量配置
ENABLE_LOG_PERSISTENCE = os.getenv("ENABLE_LOG_PERSISTENCE", "false").lower() == "true"

# 日志配置
handlers = [
    # 控制台输出 - 所有日志
    {
        "sink": sys.stdout,
        "format": "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        "level": "DEBUG",  # 改为 DEBUG 级别以显示所有日志
    }
]

# 如果启用了日志持久化，添加文件处理器
if ENABLE_LOG_PERSISTENCE:
    handlers.append({
        "sink": os.path.join(log_path, "app.log"),
        "format": "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        "level": "DEBUG",
        "rotation": "500 MB",
        "retention": "10 days",
    })

# 配置日志
config = {
    "handlers": handlers
}

# 配置日志
logger.configure(**config)

# 导出logger实例
log = logger 