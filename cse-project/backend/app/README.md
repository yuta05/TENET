# Backend README

このディレクトリには、CSEプロジェクトのバックエンドアプリケーションが含まれています。バックエンドはFastAPIを使用して構築されており、MongoDB、Redis、Milvus、OpenAI、Langchain、Tavilyなどのサービスと連携しています。

## プロジェクト構成

```
backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
├── tests/
├── .env
├── Dockerfile
├── requirements.txt
└── requirements-dev.txt
```

## 環境変数

環境変数は、プロジェクトルートの`.env`ファイルに設定します。以下の内容を参考にして、必要な環境変数を設定してください。

### `.env` の設定

```env
PROJECT_NAME=Customer Service Engine
VERSION=0.1.0
PORT=8080
ENVIRONMENT=development
# Database
MONGODB_URL=mongodb://mongodb:27017
MONGODB_DB_NAME=cse
# Redis
REDIS_URL=redis://redis:6379
# Milvus
MILVUS_HOST=milvus
MILVUS_PORT=19530
# OpenAI
OPENAI_API_KEY=your_openai_api_key
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
```

## セットアップ

### 前提条件

- Docker
- Docker Compose
- Python 3.x

### Dockerのインストール

Dockerをインストールするには、公式サイトのインストールガイドに従ってください。

- [Docker Desktop for Windows](https://docs.docker.com/desktop/windows/install/)
- [Docker Desktop for Mac](https://docs.docker.com/desktop/mac/install/)
- [Docker Engine for Linux](https://docs.docker.com/engine/install/)

### Docker Composeのインストール

Docker ComposeはDocker Desktopに含まれていますが、Linuxでは別途インストールが必要です。

- [Docker Compose Install Guide](https://docs.docker.com/compose/install/)

### Pythonのインストール

Python 3.xをインストールするには、公式サイトのインストールガイドに従ってください。

- [Python Download](https://www.python.org/downloads/)

### 開発環境のセットアップ

1. `backend` ディレクトリに移動します。

    ```sh
    cd backend
    ```

2. 必要なPythonパッケージをインストールします。

    ```sh
    pip install -r requirements.txt
    ```

3. Dockerイメージをビルドします。

    ```sh
    docker build -t backend-app .
    ```

4. コンテナを起動します。

    ```sh
    docker run -d -p 8000:8000 backend-app
    ```

### テストの実行

1. `tests` ディレクトリに移動します。

    ```sh
    cd tests
    ```

2. テストを実行します。

    ```sh
    pytest
    ```

## 使用方法

バックエンドのFastAPIアプリケーションは、デフォルトで `http://localhost:8000` でアクセスできます。

## ディレクトリ詳細

- `app/`: バックエンドアプリケーションのコードと設定ファイル。
- `tests/`: テストコード。
- `.env`: 環境変数ファイル。
- `Dockerfile`: Dockerイメージの設定ファイル。
- `requirements.txt`: プロジェクトの依存関係。
- `requirements-dev.txt`: 開発用の依存関係。

## コンテナの停止

開発環境のコンテナが不要になったら、以下のコマンドを実行してすべてのコンテナを停止します。

```sh
docker-compose down
```

## トラブルシューティング

### よくある問題と解決策

#### ビルドエラー

- npmキャッシュをクリア: `npm cache clean --force`
- `node_modules`を削除: `rm -rf node_modules`
- 依存関係を再インストール: `npm install`

#### 開発サーバーの問題

- ポートの利用状況を確認
- 環境変数を確認
- 競合するプロセスを確認