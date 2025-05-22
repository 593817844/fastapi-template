# FastAPI Template

一个基于FastAPI的项目模板，集成了MySQL、Redis、日志系统和中间件。本项目提供了一个完整的后端服务框架，包含用户认证、数据缓存、错误处理等常用功能。

## 功能特性

- FastAPI Web框架
- Tortoise ORM (MySQL)
- Redis缓存
- 日志系统 (loguru)
  - 支持控制台彩色输出
  - 可配置的日志持久化
  - 日志文件自动轮转
- 请求耗时中间件
- 环境配置管理
- 统一错误处理

## 项目结构

```
.
├── app/
│   ├── core/                 # 核心功能模块
│   │   ├── config/          # 配置管理
│   │   │   ├── settings.py  # 环境配置
│   │   │   └── __init__.py
│   │   ├── database.py      # 数据库配置
│   │   ├── logger.py        # 日志配置
│   │   ├── middleware.py    # 中间件
│   │   ├── redis.py         # Redis配置
│   │   └── exceptions.py    # 错误处理
│   ├── models/              # 数据模型
│   │   └── user.py         # 用户模型
│   ├── routers/            # 路由模块
│   │   └── user.py         # 用户路由
│   ├── schemas/            # 数据验证
│   │   └── user.py         # 用户模式
│   └── main.py             # 主应用
├── logs/                   # 日志文件
├── tests/                  # 测试文件
├── .env.example           # 环境变量示例
├── requirements.txt       # 项目依赖
├── start.sh              # 启动脚本
└── run.py                # 应用入口
```

## 开发环境要求

- Python 3.8+
- MySQL 5.7+
- Redis 6.0+
- Linux/Unix 环境（推荐）

## 安装

1. 克隆项目
```bash
git clone <repository_url>
cd fastapi-template
```

2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，设置必要的环境变量
```

## 开发指南

### 1. 启动开发服务器

```bash
# 开发环境
./start.sh dev

# 生产环境
./start.sh prod
```

### 2. 添加新的路由

1. 在 `app/routers/` 目录下创建新的路由文件
2. 在路由文件中定义API端点
3. 在 `app/main.py` 中注册路由

示例：
```python
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/items", tags=["items"])

@router.get("/")
async def get_items():
    return {"items": []}
```

### 3. 添加新的模型

1. 在 `app/models/` 目录下创建新的模型文件
2. 定义模型类
3. 在 `app/core/database.py` 中注册模型

示例：
```python
from tortoise import fields, models

class Item(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    description = fields.TextField()
```

## 部署指南

### 1. 使用 Docker Compose 部署

1. 启动所有服务
```bash
docker-compose up -d
```

2. 查看日志
```bash
docker-compose logs -f
```

### 2. 手动部署

1. 安装依赖
```bash
pip install -r requirements.txt
```

2. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件
```

3. 启动应用
```bash
./start.sh prod
```

### 3. 使用 Nginx 反向代理

```nginx
server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## API文档

启动服务后访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 日志

日志系统基于 loguru 实现，具有以下特性：

1. 日志输出
   - 控制台彩色输出（开发环境）
   - 文件持久化（可选）

2. 日志配置
   - 通过环境变量 `ENABLE_LOG_PERSISTENCE` 控制是否启用日志持久化
   - 默认值：false（不启用持久化）
   - 启用方式：`export ENABLE_LOG_PERSISTENCE=true`

3. 日志文件
   - 位置：`logs/` 目录
   - 自动轮转：单个文件最大 500MB
   - 保留时间：10天

4. 日志格式
   - 时间戳
   - 日志级别
   - 模块名
   - 函数名
   - 行号
   - 日志内容

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License 