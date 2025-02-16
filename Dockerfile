FROM ubuntu:latest
USER root

SHELL ["/bin/bash", "-c"]
WORKDIR /app

# 替换软件源并安装依赖
RUN --mount=type=cache,id=one_apt,target=/var/cache/apt,sharing=locked \
    apt update && \
    apt install -y --no-install-recommends \
        ca-certificates libglib2.0-0 libglx-mesa0 libgl1 \
        pkg-config libicu-dev libgdiplus default-jdk \
        libatk-bridge2.0-0 libpython3-dev libgtk-4-1 libnss3 xdg-utils libgbm-dev \
        python3-pip pipx nginx unzip curl wget git vim less && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# 配置 pip 和 uv
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip3 config set global.trusted-host pypi.tuna.tsinghua.edu.cn && \
    pipx install uv

ENV PYTHONDONTWRITEBYTECODE=1 DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1
ENV UV_INDEX=https://pypi.tuna.tsinghua.edu.cn/simple
ENV PATH=/root/.local/bin:$PATH
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

# 安装 Python 依赖
COPY pyproject.toml uv.lock ./
RUN uv sync --python 3.12 --frozen




# 配置入口点
COPY server /app/server
COPY docker/entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]
