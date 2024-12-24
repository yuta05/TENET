import os
import subprocess
from database import initialize_database  # 既に移動済みの関数をインポート

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

def setup_services():
    print("Creating .env files...")
    run_command('python env_setup.py')  # env_setup.py を実行

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