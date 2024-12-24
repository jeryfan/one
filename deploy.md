### 构建 web 镜像

cd web/ui
docker build -t one-ui .

### 使用代理

docker build --build-arg http_proxy=http://192.168.0.108:7890 --build-arg https_proxy=http://192.168.0.108:7890 -t one-ui .

### 构建 server 镜像

docker build -t one-server .

### 使用代理

docker build --build-arg http_proxy=http://192.168.0.108:7890 --build-arg https_proxy=http://192.168.0.108:7890 -t one-server .

### 启动

cd docker
docker-compose up -d
