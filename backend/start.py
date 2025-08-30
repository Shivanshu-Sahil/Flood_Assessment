#!/usr/bin/env python3
"""
Startup script for the Flood Detection Backend API
"""
import uvicorn
import os
import sys
from pathlib import Path
import subprocess

# Add the backend directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent))

def install_dependencies():
    """Install dependencies from requirements.txt."""
    requirements_path = Path(__file__).resolve().parent / "requirements.txt"
    if requirements_path.exists():
        print("Installing dependencies from requirements.txt...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(requirements_path)])
            print("Dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            sys.exit(1)
    else:
        print("requirements.txt not found. Skipping dependency installation.")

if __name__ == "__main__":
    # Install dependencies
    install_dependencies()

    # Get port from environment or use default
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")

    print(f"Starting Flood Detection Backend API on {host}:{port}")
    print("API Documentation will be available at:")
    print(f"  - Swagger UI: http://{host}:{port}/docs")
    print(f"  - ReDoc: http://{host}:{port}/redoc")
    print(f"  - OpenAPI JSON: http://{host}:{port}/openapi.json")

    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )
