"""
APEX: Agentic Portrait EXperience

A comprehensive professional portrait generation system using AI models.
"""

__version__ = "2.0.0"
__author__ = "APEX Development Team"
__description__ = "Agentic Portrait EXperience - AI-powered professional portrait generation"

from .core.profile_manager import ProfileManager
from .core.prompt_generator import PromptGenerator
from .ui.gradio_interface import create_interface
from .models.profile import Profile, ProfileData

__all__ = [
    "ProfileManager",
    "PromptGenerator", 
    "create_interface",
    "Profile",
    "ProfileData"
]
