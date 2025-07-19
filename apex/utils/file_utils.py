"""
Utility functions for APEX.
"""

import os
import shutil
from typing import Optional

def ensure_directory(path: str) -> None:
    """Ensure a directory exists, create if it doesn't."""
    os.makedirs(path, exist_ok=True)

def copy_file(src: str, dst: str) -> bool:
    """Copy a file from source to destination."""
    try:
        shutil.copy2(src, dst)
        return True
    except (IOError, OSError):
        return False

def get_file_size(filepath: str) -> Optional[int]:
    """Get file size in bytes."""
    try:
        return os.path.getsize(filepath)
    except OSError:
        return None

def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format."""
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f}{size_names[i]}"

def sanitize_filename(filename: str) -> str:
    """Sanitize filename by removing invalid characters."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename.strip()
