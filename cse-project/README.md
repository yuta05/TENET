# CSE Project

このプロジェクトは、FastAPIを使用したバックエンドと、フロントエンド、そしていくつかのサービス（Milvus、MongoDB、Redis）を含むフルスタックアプリケーションです。

## プロジェクト構成
```
/cse-project
├── docker-compose.yml
├── frontend/
│   └── .env.example
│   └── Dockerfile
├── backend/
│   └── .env.example
│   └── Dockerfile
├── db/
│   └── sample_data.sql
```
## セットアップ

### 前提条件

- Docker
- Docker Compose
- Python 3.x

#### Dockerのインストール

Dockerをインストールするには、公式サイトのインストールガイドに従ってください。

- [Docker Desktop for Windows](https://docs.docker.com/desktop/windows/install/)
- [Docker Desktop for Mac](https://docs.docker.com/desktop/mac/install/)
- [Docker Engine for Linux](https://docs.docker.com/engine/install/)

#### Docker Composeのインストール

Docker ComposeはDocker Desktopに含まれていますが、Linuxでは別途インストールが必要です。

- [Docker Compose Install Guide](https://docs.docker.com/compose/install/)

#### Pythonのインストール

Python 3.xをインストールするには、公式サイトのインストールガイドに従ってください。

- [Python Download](https://www.python.org/downloads/)

### 環境変数

環境変数はそれぞれのディレクトリにある `.env` ファイルに設定します。`.env` ファイルの例は `.env.example` ファイルにあり、このファイルが `setup.py` によって参照されます。以下の内容を参考にして、必要な環境変数を設定してください。

```sh
python env_setup.py
```
このコマンドを実行して .env ファイルを自動的に作成することができますが、手動で作成しても構いません。

#### `./backend/.env` の設定

```env
PROJECT_NAME=Customer Service Engine
VERSION=0.1.0
PORT=8080
ENVIRONMENT=development
DATABASE_URL=/app/db/sample_data.db
NODE_ENV=development
# OpenAI
OPENAI_API_KEY=your_openai_api_key
# Anthropic
ANTHROPIC_API_KEY=your_anthropic_api_key
# Langchain
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2="true"
# Tavily
TAVILY_API_KEY=your_tavily_api_key
# Security
JWT_SECRET=your_jwt_secret
JWT_ALGORITHM=HS256
# CORS
ALLOWED_ORIGINS=["http://localhost:3000"]
BACKEND_PORT=8000
```

#### `./frontend/.env` の設定

```env
VITE_APP_NAME=CSE Frontend
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000/ws
VITE_APP_VERSION=0.1.0
VITE_DEBUG=true
NODE_ENV=development
```

### 開発環境のセットアップ

1. プロジェクトルートに移動します。

    ```sh
    cd cse-project
    ```

2. 開発環境用のDockerコンテナをビルドして起動するためのヘルパースクリプトを実行します。

    ```sh
    python setup.py
    ```

### 開発環境のセットアップでうまくいかなかった場合

以下の手順に従って、手動でセットアップを行ってください。

#### バックエンドのセットアップ (手動)

1. `backend` ディレクトリに移動します。

    ```sh
    cd backend
    ```

2. Dockerイメージをビルドします。

    ```sh
    docker build -t backend-app .
    ```

3. コンテナを起動します。

    ```sh
    docker run -d -p 8000:8000 backend-app
    ```

#### フロントエンドのセットアップ (手動)

1. `frontend` ディレクトリに移動します。

    ```sh
    cd frontend
    ```

2. Dockerイメージをビルドします。

    ```sh
    docker build -t frontend-app .
    ```

3. コンテナを起動します。

    ```sh
    docker run -d -p 3000:3000 frontend-app
    ```

#### サービスのセットアップ (手動)

1. プロジェクトルートに戻ります。

    ```sh
    cd ..
    ```

2. Docker Composeを使用してサービスを起動します。

    ```sh
    docker-compose up -d
    ```

3. データベースを初期化します。

    ```sh
    python -c "from setup import initialize_database; initialize_database('./db/sample_data.db', 'sample_data.sql')"
    ```

## 使用方法

バックエンドのFastAPIアプリケーションは、デフォルトで `http://localhost:8000` でアクセスできます。フロントエンドアプリケーションは、デフォルトで `http://localhost:3000` でアクセスできます。

## コンテナの停止

開発環境のコンテナが不要になったら、以下のコマンドを実行してすべてのコンテナを停止します。

1. プロジェクトルートに移動します。

    ```sh
    cd cse-project
    ```

2. Docker Composeを使用してコンテナを停止します。

    ```sh
    docker-compose down
    ```

## ディレクトリ詳細

- `backend/`: バックエンドアプリケーションのコードと設定ファイル。
- `frontend/`: フロントエンドアプリケーションのコードと設定ファイル。
- `db/`: データベースの初期化スクリプトとデータベースファイル。
- `docker-compose.yml`: Docker Compose設定ファイル。