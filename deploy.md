### 构建 web 镜像

cd web/ui
docker build -t one-ui .

### 使用代理

docker build --build-arg http_proxy=http://127.0.0.1:7890 --build-arg https_proxy=http://127.0.0.1:7890 -t one-ui .

### 启动

cd docker
docker-compose up -d
