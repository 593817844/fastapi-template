# 镜像名称（可通过命令行覆盖）
IMAGE_NAME ?= your-docker-repo/infer-api
# 镜像标签
TAG = $(shell date +%Y%m%d%H%M)

# 构建 Docker 镜像，指定 Dockerfile 路径
build:
	docker build -f deploy/Dockerfile -t $(IMAGE_NAME):$(TAG) .

# 推送 Docker 镜像到仓库
push:
	docker push $(IMAGE_NAME):$(TAG)

.PHONY: build push

## 用法
## make build IMAGE_NAME=your-docker-repo/api
## make push IMAGE_NAME=your-docker-repo/api
