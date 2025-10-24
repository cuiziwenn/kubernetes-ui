# ----------------------------
# Stage 1: Build Environment
# ----------------------------
FROM python:3.11-slim AS builder

# 设置国内 apt 源
RUN echo "deb http://mirrors.aliyun.com/debian/ bookworm main contrib non-free non-free-firmware" > /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libssl-dev \
        libffi-dev \
        python3-dev \
        curl \
        ca-certificates \
        git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 拷贝依赖文件
COPY requirements.txt .

# 创建独立虚拟环境并安装 Python 包
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# ----------------------------
# Stage 2: Final Image
# ----------------------------
FROM python:3.11-slim

# 设置国内 apt 源（安装 ca-certificates）
RUN echo "deb http://mirrors.aliyun.com/debian/ bookworm main contrib non-free non-free-firmware" > /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 拷贝虚拟环境
COPY --from=builder /opt/venv /opt/venv
# 拷贝应用代码
COPY . .

# 使用非 root 用户
RUN useradd -m appuser
USER appuser

# 设置 PATH 使用虚拟环境
ENV PATH="/opt/venv/bin:$PATH"

# 容器启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
