# CSE Project

このプロジェクトは、FastAPIを使用したバックエンドと、フロントエンド、そしていくつかのサービス（Milvus、MongoDB、Redis）を含むフルスタックアプリケーションです。

## プロジェクト構成
'''
/cse-project
├── docker-compose.yml
├── .env
├── frontend/
│   └── Dockerfile
├── backend/
│   └── Dockerfile
└── services/
    ├── mongodb/
    ├── redis/
    └── milvus/
'''
## セットアップ

### 前提条件

- Docker
- Docker Compose

### 環境変数

プロジェクトルートにある `.env` ファイルに必要な環境変数を設定します。

### バックエンドのセットアップ

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

### フロントエンドのセットアップ

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

### サービスのセットアップ

1. プロジェクトルートに戻ります。

    ```sh
    cd ..
    ```

2. Docker Composeを使用してサービスを起動します。

    ```sh
    docker-compose up -d
    ```

## 使用方法

バックエンドのFastAPIアプリケーションは、デフォルトで `http://localhost:8080` でアクセスできます。フロントエンドアプリケーションは、デフォルトで `http://localhost:3000` でアクセスできます。

## ディレクトリ詳細

- `backend/`: バックエンドアプリケーションのコードと設定ファイル。
- `frontend/`: フロントエンドアプリケーションのコードと設定ファイル。
- `services/`: 各種サービス（Milvus、MongoDB、Redis）の設定ファイル。
- `docker-compose.yml`: Docker Compose設定ファイル。
- `.env`: 環境変数ファイル。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。
