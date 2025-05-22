#!/bin/bash

# 开发环境配置
export_dev() {
    # App settings
    export APP_HOST=0.0.0.0
    export APP_PORT=8000
    export DEBUG=True

    # Server settings
    export WORKERS_COUNT=1
    export WORKER_CONNECTIONS=100
    export KEEPALIVE=5

    # Database settings
    export DB_HOST=localhost
    export DB_PORT=13306
    export DB_USER=fastapi
    export DB_PASSWORD=fastapi123
    export DB_NAME=fastapi_db

    # Redis settings
    export REDIS_HOST=localhost
    export REDIS_PORT=16379
    export REDIS_DB=0
    export REDIS_PASSWORD=redis123
}

# 生产环境配置
export_prod() {
    # App settings
    export APP_HOST=0.0.0.0
    export APP_PORT=8000
    export DEBUG=False

    # Server settings
    export WORKERS_COUNT=4
    export WORKER_CONNECTIONS=1000
    export KEEPALIVE=5

    # Database settings
    export DB_HOST=localhost
    export DB_PORT=13306
    export DB_USER=fastapi
    export DB_PASSWORD=fastapi123
    export DB_NAME=fastapi_db

    # Redis settings
    export REDIS_HOST=localhost
    export REDIS_PORT=16379
    export REDIS_DB=0
    export REDIS_PASSWORD=redis123
}

# 根据参数选择环境
case "$1" in
    "dev")
        export_dev
        echo "Starting in development environment..."
        ;;
    "prod")
        export_prod
        echo "Starting in production environment..."
        ;;
    *)
        echo "Usage: $0 {dev|prod}"
        exit 1
        ;;
esac

# 启动应用
python3 run.py 