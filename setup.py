#!/usr/bin/env python3
"""
Setup script for APEX development environment.
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"📦 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def setup_environment():
    """Set up the development environment."""
    print("🖼️ Setting up APEX development environment")
    print("=" * 50)
    
    # Create virtual environment if it doesn't exist
    if not os.path.exists(".venv"):
        if not run_command("python -m venv .venv", "Creating virtual environment"):
            return False
    
    # Determine activation script based on OS
    if sys.platform == "win32":
        activate_script = ".venv\\Scripts\\activate"
        pip_command = ".venv\\Scripts\\pip"
    else:
        activate_script = ".venv/bin/activate"
        pip_command = ".venv/bin/pip"
    
    # Install dependencies
    if not run_command(f"{pip_command} install --upgrade pip", "Upgrading pip"):
        return False
    
    # Try main requirements first, fall back to minimal if conflicts
    print("📦 Attempting to install main requirements...")
    if not run_command(f"{pip_command} install -r requirements.txt", "Installing main dependencies"):
        print("⚠️  Main requirements failed, trying minimal requirements...")
        if not run_command(f"{pip_command} install -r requirements-minimal.txt", "Installing minimal dependencies"):
            print("❌ Both requirement files failed. Please install manually:")
            print("   pip install gradio numpy pillow requests")
            return False
        else:
            print("✅ Minimal dependencies installed successfully")
            print("💡 You can manually install additional packages later:")
            print("   pip install torch transformers diffusers opencv-python")
    
    # Create necessary directories
    directories = [
        "data/profiles",
        "data/uploads", 
        "logs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"📁 Created directory: {directory}")
    
    print("\n🎉 Setup completed successfully!")
    print(f"🚀 To start the application, run: python app.py")
    print(f"🌐 Or activate the virtual environment first:")
    
    if sys.platform == "win32":
        print(f"   {activate_script}")
    else:
        print(f"   source {activate_script}")
    
    return True

def run_tests():
    """Run the test suite."""
    print("\n🧪 Running tests...")
    return run_command("python -m pytest tests/ -v", "Running test suite")

def main():
    """Main setup function."""
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        setup_environment()

if __name__ == "__main__":
    main()
