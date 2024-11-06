FROM python:3.9-slim

WORKDIR /app

# システムの依存関係をインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python パッケージをインストール
COPY requirements.txt requirements-dev.txt ./

# 開発環境の場合は両方のrequirementsをインストール
ARG ENVIRONMENT=production
RUN if [ "$ENVIRONMENT" = "development" ] ; then \
        pip install --no-cache-dir -r requirements-dev.txt ; \
    else \
        pip install --no-cache-dir -r requirements.txt ; \
    fi

# アプリケーションコードをコピー
COPY . .

# FastAPI アプリケーションを起動
CMD if [ "$ENVIRONMENT" = "development" ] ; then \
        uvicorn main:app --host 0.0.0.0 --port 8000 --reload ; \
    else \
        uvicorn main:app --host 0.0.0.0 --port 8000 ; \
    fi