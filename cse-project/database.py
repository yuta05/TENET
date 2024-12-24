import sqlite3

def initialize_database(db_path, sql_script_path):    
    with sqlite3.connect(db_path) as conn:
        with open(sql_script_path, 'r') as f:
            conn.executescript(f.read())
    print(f"Database initialized at {db_path}")