import os
import shutil
import subprocess
import sqlite3

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
        if result.stderr:
            print(result.stderr.decode())
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        print(e.output.decode())
        print(e.stderr.decode())
        raise

def copy_env_example(src, dest):
    if os.path.exists(src):
        shutil.copy(src, dest)
        print(f"{dest} created successfully from {src}.")
    else:
        print(f"{src} does not exist. Please create the file first.")

def create_env_files():
    # Paths to .env.example and target .env files
    frontend_env_example = './frontend/.env.example'
    backend_env_example = './backend/.env.example'
    frontend_env = './frontend/.env'
    backend_env = './backend/.env'

    # Create .env files by copying .env.example
    copy_env_example(frontend_env_example, frontend_env)
    copy_env_example(backend_env_example, backend_env)

def initialize_database(db_path, sql_script_path):    
    with sqlite3.connect(db_path) as conn:
        with open(sql_script_path, 'r') as f:
            conn.executescript(f.read())
    print(f"Database initialized at {db_path}")

def setup_services():
    print("Creating .env files...")
    create_env_files()

    print("Stopping any running containers...")
    run_command('docker-compose down')

    print("Building and running all containers in development mode...")
    run_command('docker-compose up --build -d')

    print("Initializing the database...")
    initialize_database('./backend/app/db/sample_data.db', './backend/app/db/sample_data.sql')

    print("\nSetup completed successfully!")
    print("Frontend is accessible at: http://localhost:3000/")
    print("Backend is accessible at: http://localhost:8000/")

def main():
    setup_services()

if __name__ == "__main__":
    main()