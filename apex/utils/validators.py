"""
Validation utilities for APEX.
"""

import re
from typing import Dict, Any, List, Tuple

class Validator:
    """Validation utilities for profile data."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_resolution(resolution: str) -> bool:
        """Validate resolution format."""
        valid_resolutions = [
            "1024x1024 (Standard)",
            "1536x1024 (Wide)", 
            "1024x1536 (Portrait)",
            "2048x2048 (High-Res)"
        ]
        return resolution in valid_resolutions
    
    @staticmethod
    def validate_required_fields(data: Dict[str, Any], required_fields: List[str]) -> Tuple[bool, List[str]]:
        """Validate that required fields are present and not empty."""
        missing_fields = []
        
        for field in required_fields:
            if field not in data or not data[field] or str(data[field]).strip() == "":
                missing_fields.append(field)
        
        return len(missing_fields) == 0, missing_fields
    
    @staticmethod
    def validate_choice_field(value: str, valid_choices: List[str]) -> bool:
        """Validate that a value is in the list of valid choices."""
        return value in valid_choices
    
    @staticmethod
    def validate_custom_notes_length(notes: str, max_length: int = 1000) -> bool:
        """Validate custom notes length."""
        return len(notes.strip()) <= max_length
