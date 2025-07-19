"""
Data models for APEX profile system.
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any, Tuple
from datetime import datetime

@dataclass
class BasicInfo:
    """Basic portrait information."""
    purpose: str
    attire: str
    background: str
    vibe: str

@dataclass
class AdvancedSettings:
    """Advanced portrait settings."""
    lighting: str = "Professional Flash"
    mood: str = "Professional"
    age_range: str = "Not Specified"
    gender: str = "Not Specified"
    ethnicity: str = "Not Specified"
    resolution: str = "1024x1024 (Standard)"

@dataclass
class AdditionalInfo:
    """Additional profile information."""
    reference_photo: Optional[str] = None
    custom_notes: Optional[str] = None
    preset_used: Optional[str] = None

@dataclass
class Metadata:
    """Profile metadata."""
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    version: str = "2.0"
    created_by: str = "APEX Portrait Generator"

@dataclass
class ProfileData:
    """Complete profile data structure."""
    basic_info: BasicInfo
    advanced_settings: AdvancedSettings
    additional_info: AdditionalInfo
    metadata: Metadata
    generated_prompt: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert profile to dictionary."""
        return {
            "basic_info": {
                "purpose": self.basic_info.purpose,
                "attire": self.basic_info.attire,
                "background": self.basic_info.background,
                "vibe": self.basic_info.vibe
            },
            "advanced_settings": {
                "lighting": self.advanced_settings.lighting,
                "mood": self.advanced_settings.mood,
                "age_range": self.advanced_settings.age_range,
                "gender": self.advanced_settings.gender,
                "ethnicity": self.advanced_settings.ethnicity,
                "resolution": self.advanced_settings.resolution
            },
            "additional_info": {
                "reference_photo": self.additional_info.reference_photo,
                "custom_notes": self.additional_info.custom_notes,
                "preset_used": self.additional_info.preset_used
            },
            "metadata": {
                "timestamp": self.metadata.timestamp,
                "version": self.metadata.version,
                "created_by": self.metadata.created_by
            },
            "generated_prompt": self.generated_prompt
        }

class Profile:
    """Profile utility class for validation and operations."""
    
    @staticmethod
    def validate_basic_info(purpose: str, attire: str, background: str, vibe: str) -> Tuple[bool, str]:
        """Validate basic profile information."""
        if not purpose:
            return False, "⚠️ Please select a purpose for your portrait"
        if not attire:
            return False, "⚠️ Please select your preferred attire"
        if not background:
            return False, "⚠️ Please select a background style"
        if not vibe:
            return False, "⚠️ Please select your desired vibe"
        return True, "✅ All inputs valid"
    
    @staticmethod
    def create_profile(purpose: str, attire: str, background: str, vibe: str,
                      lighting: str = "Professional Flash", mood: str = "Professional",
                      age_range: str = "Not Specified", gender: str = "Not Specified",
                      ethnicity: str = "Not Specified", resolution: str = "1024x1024 (Standard)",
                      reference_photo: Optional[str] = None, custom_notes: Optional[str] = None,
                      preset_used: Optional[str] = None) -> ProfileData:
        """Create a ProfileData instance."""
        return ProfileData(
            basic_info=BasicInfo(purpose, attire, background, vibe),
            advanced_settings=AdvancedSettings(lighting, mood, age_range, gender, ethnicity, resolution),
            additional_info=AdditionalInfo(reference_photo, custom_notes, preset_used),
            metadata=Metadata()
        )
