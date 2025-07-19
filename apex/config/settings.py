"""
Configuration settings for APEX.
"""

import os
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class UIConfig:
    """UI configuration settings."""
    title: str = "APEX Portrait Generator"
    theme: str = "default"
    port: int = 7860
    host: str = "127.0.0.1"
    share: bool = True
    inbrowser: bool = True
    max_file_size: int = 10 * 1024 * 1024  # 10MB

@dataclass
class ProfileConfig:
    """Profile configuration settings."""
    profiles_dir: str = "data/profiles"
    uploads_dir: str = "data/uploads"
    max_profiles: int = 1000
    auto_save: bool = True

@dataclass
class PromptConfig:
    """Prompt generation configuration."""
    max_prompt_length: int = 500
    include_negative_prompt: bool = True
    quality_tags: List[str] = None
    
    def __post_init__(self):
        if self.quality_tags is None:
            self.quality_tags = [
                "masterpiece",
                "best quality", 
                "highly detailed",
                "photorealistic"
            ]

class Config:
    """Main configuration class."""
    
    def __init__(self):
        self.ui = UIConfig()
        self.profile = ProfileConfig()
        self.prompt = PromptConfig()
        
        # Load from environment if available
        self._load_from_env()
    
    def _load_from_env(self):
        """Load configuration from environment variables."""
        # UI settings
        self.ui.port = int(os.getenv('APEX_PORT', self.ui.port))
        self.ui.host = os.getenv('APEX_HOST', self.ui.host)
        self.ui.share = os.getenv('APEX_SHARE', str(self.ui.share)).lower() == 'true'
        
        # Profile settings
        self.profile.profiles_dir = os.getenv('APEX_PROFILES_DIR', self.profile.profiles_dir)
        self.profile.uploads_dir = os.getenv('APEX_UPLOADS_DIR', self.profile.uploads_dir)
        self.profile.auto_save = os.getenv('APEX_AUTO_SAVE', str(self.profile.auto_save)).lower() == 'true'

# Global configuration instance
config = Config()
