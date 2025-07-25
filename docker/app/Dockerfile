FROM python:3.11-slim

WORKDIR /app

# 设置环境变量
ENV PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    TZ=Asia/Shanghai

# 安装系统依赖
# 配置国内 apt 镜像源 (阿里云)
RUN rm -f /etc/apt/sources.list.d/* \
    && echo "deb https://mirrors.aliyun.com/debian/ bullseye main contrib non-free" > /etc/apt/sources.list \
    && echo "deb-src https://mirrors.aliyun.com/debian/ bullseye main contrib non-free" >> /etc/apt/sources.list \
    && apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY requirements.txt .
COPY app/ app/
COPY start.sh .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 创建日志目录
RUN mkdir -p logs

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["bash", "start.sh"] 
