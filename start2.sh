#!/bin/bash

# 开发环境配置
export_dev() {
    # API Token
    export DEBUG=True
}

# 生产环境配置
export_prod() {
    export DEBUG=False
}

# 根据参数选择环境
case "$1" in
    "dev")
        export_dev
        echo "Starting in development environment..."
        uvicorn app.main:app \
        --host 0.0.0.0 \
        --port 8000 \
        --reload \
        --log-level debug
        ;;
    "prod")
        export_prod
        echo "Starting in production environment with Gunicorn..."
        gunicorn app.main:app \
        --bind=0.0.0.0:8000 \
        --workers=4 \
        --worker-class=uvicorn.workers.UvicornWorker \
        --worker-connections=1000 \
        --keep-alive=5 \
        --max-requests=1000 \
        --timeout=60 \
        --graceful-timeout=30 \
        --access-logfile=- \
        --error-logfile=- \
        --log-level=info
        ;;
    *)
        echo "Usage: $0 {dev|prod}"
        exit 1
        ;;
esac 
