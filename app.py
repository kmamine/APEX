#!/usr/bin/env python3
"""
APEX: Agentic Portrait EXperience
Main application entry point.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from apex.ui.gradio_interface import create_interface
from apex.config.settings import config

def main():
    """Main application entry point."""
    print("🖼️ Starting APEX: Agentic Portrait EXperience")
    print(f"📊 Version: 2.0.0")
    print(f"🌐 Host: {config.ui.host}:{config.ui.port}")
    print(f"📁 Profiles directory: {config.profile.profiles_dir}")
    print("-" * 50)
    
    # Create and launch the interface
    demo = create_interface()
    demo.launch(
        share=config.ui.share,
        inbrowser=config.ui.inbrowser,
        show_error=True,
        server_name=config.ui.host,
        server_port=config.ui.port,
        favicon_path=None,
        app_kwargs={"docs_url": "/docs", "redoc_url": "/redoc"}
    )

if __name__ == "__main__":
    main()
