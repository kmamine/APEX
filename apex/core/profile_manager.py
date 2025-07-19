"""
Profile management and file operations.
"""

import json
import os
from datetime import datetime
from typing import Dict, Any, Optional, Tuple
from ..models.profile import ProfileData, Profile

class ProfileManager:
    """Manages profile creation, validation, and file operations."""
    
    def __init__(self, profiles_dir: str = "data/profiles"):
        self.profiles_dir = profiles_dir
        self._ensure_directory_exists()
    
    def _ensure_directory_exists(self):
        """Ensure the profiles directory exists."""
        os.makedirs(self.profiles_dir, exist_ok=True)
    
    def create_profile(self, purpose: str, attire: str, background: str, vibe: str,
                      lighting: str = "Professional Flash", mood: str = "Professional",
                      age_range: str = "Not Specified", gender: str = "Not Specified",
                      ethnicity: str = "Not Specified", resolution: str = "1024x1024 (Standard)",
                      photo_path: Optional[str] = None, custom_notes: str = "",
                      preset_name: Optional[str] = None) -> Tuple[ProfileData, bool, str]:
        """
        Create and validate a profile.
        
        Returns:
            Tuple: (ProfileData, is_valid, message)
        """
        # Validate basic inputs
        is_valid, message = Profile.validate_basic_info(purpose, attire, background, vibe)
        if not is_valid:
            return None, False, message
        
        # Create profile data
        profile = Profile.create_profile(
            purpose=purpose,
            attire=attire,
            background=background,
            vibe=vibe,
            lighting=lighting,
            mood=mood,
            age_range=age_range,
            gender=gender,
            ethnicity=ethnicity,
            resolution=resolution,
            reference_photo="uploaded" if photo_path else None,
            custom_notes=custom_notes.strip() if custom_notes else None,
            preset_used=preset_name
        )
        
        return profile, True, "✅ Profile created successfully"
    
    def save_profile(self, profile_data: ProfileData, filename: Optional[str] = None) -> str:
        """Save profile to JSON file."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"portrait_profile_{timestamp}.json"
        
        if not filename.endswith('.json'):
            filename += '.json'
        
        filepath = os.path.join(self.profiles_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(profile_data.to_dict(), f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def load_profile(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load profile from JSON file."""
        filepath = os.path.join(self.profiles_dir, filename)
        
        if not os.path.exists(filepath):
            return None
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return None
    
    def list_profiles(self) -> list[str]:
        """List all saved profiles."""
        if not os.path.exists(self.profiles_dir):
            return []
        
        return [f for f in os.listdir(self.profiles_dir) if f.endswith('.json')]
    
    def delete_profile(self, filename: str) -> bool:
        """Delete a profile file."""
        filepath = os.path.join(self.profiles_dir, filename)
        
        if os.path.exists(filepath):
            try:
                os.remove(filepath)
                return True
            except OSError:
                return False
        return False
    
    def get_presets(self) -> Dict[str, Dict[str, str]]:
        """Get predefined profile presets."""
        return {
            "LinkedIn Professional": {
                "purpose": "LinkedIn",
                "attire": "Business Formal",
                "background": "Corporate Office",
                "vibe": "Confident",
                "custom_notes": "Professional headshot for LinkedIn profile with clean, corporate appearance"
            },
            "Creative Portfolio": {
                "purpose": "Personal Branding",
                "attire": "Creative Professional",
                "background": "Creative Space",
                "vibe": "Creative",
                "custom_notes": "Artistic and creative portrait showcasing personality and creativity"
            },
            "Academic Professional": {
                "purpose": "Corporate Website",
                "attire": "Academic",
                "background": "Library/Academic",
                "vibe": "Sophisticated",
                "custom_notes": "Professional academic portrait for university or research profile"
            },
            "Startup Founder": {
                "purpose": "Personal Branding",
                "attire": "Smart Casual",
                "background": "Creative Space",
                "vibe": "Approachable",
                "custom_notes": "Modern, approachable portrait for startup founder or entrepreneur"
            },
            "Executive Portrait": {
                "purpose": "Corporate Website",
                "attire": "Business Formal",
                "background": "Corporate Office",
                "vibe": "Authoritative",
                "custom_notes": "High-level executive portrait conveying leadership and authority"
            }
        }
    
    def apply_preset(self, preset_name: str) -> Optional[Dict[str, str]]:
        """Apply a preset configuration."""
        presets = self.get_presets()
        return presets.get(preset_name)
