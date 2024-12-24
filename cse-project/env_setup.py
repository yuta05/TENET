import os
import shutil

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

if __name__ == "__main__":
    create_env_files()