import sqlite3
import os

def initialize_database(db_path, sql_script_path):
    # 既存のデータベースファイルを削除
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Existing database at {db_path} has been removed.")
    
    # 新しいデータベースを初期化
    with sqlite3.connect(db_path) as conn:
        with open(sql_script_path, 'r') as f:
            conn.executescript(f.read())
    print(f"Database initialized at {db_path}")