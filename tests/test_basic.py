"""
Basic tests for APEX functionality.
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apex.models.profile import Profile, ProfileData, BasicInfo, AdvancedSettings, AdditionalInfo, Metadata
from apex.core.profile_manager import ProfileManager
from apex.core.prompt_generator import PromptGenerator

class TestProfile(unittest.TestCase):
    """Test Profile class functionality."""
    
    def test_validate_basic_info_valid(self):
        """Test validation with valid inputs."""
        is_valid, message = Profile.validate_basic_info("LinkedIn", "Business Formal", "Corporate Office", "Confident")
        self.assertTrue(is_valid)
        self.assertEqual(message, "✅ All inputs valid")
    
    def test_validate_basic_info_invalid(self):
        """Test validation with invalid inputs."""
        is_valid, message = Profile.validate_basic_info("", "Business Formal", "Corporate Office", "Confident")
        self.assertFalse(is_valid)
        self.assertIn("purpose", message)
    
    def test_create_profile(self):
        """Test profile creation."""
        profile = Profile.create_profile("LinkedIn", "Business Formal", "Corporate Office", "Confident")
        self.assertIsInstance(profile, ProfileData)
        self.assertEqual(profile.basic_info.purpose, "LinkedIn")
        self.assertEqual(profile.basic_info.attire, "Business Formal")

class TestProfileManager(unittest.TestCase):
    """Test ProfileManager functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.manager = ProfileManager("test_profiles")
    
    def test_create_profile_valid(self):
        """Test creating a valid profile."""
        profile, is_valid, message = self.manager.create_profile(
            "LinkedIn", "Business Formal", "Corporate Office", "Confident"
        )
        self.assertTrue(is_valid)
        self.assertIsInstance(profile, ProfileData)
    
    def test_create_profile_invalid(self):
        """Test creating an invalid profile."""
        profile, is_valid, message = self.manager.create_profile(
            "", "Business Formal", "Corporate Office", "Confident"
        )
        self.assertFalse(is_valid)
        self.assertIsNone(profile)
    
    def test_get_presets(self):
        """Test getting presets."""
        presets = self.manager.get_presets()
        self.assertIsInstance(presets, dict)
        self.assertIn("LinkedIn Professional", presets)

class TestPromptGenerator(unittest.TestCase):
    """Test PromptGenerator functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.generator = PromptGenerator()
    
    def test_generate_prompt(self):
        """Test prompt generation."""
        profile_data = {
            'purpose': 'LinkedIn',
            'attire': 'Business Formal',
            'background': 'Corporate Office',
            'vibe': 'Confident',
            'lighting': 'Professional Flash',
            'mood': 'Professional',
            'custom_notes': 'Test notes'
        }
        prompt = self.generator.generate_prompt(profile_data)
        self.assertIsInstance(prompt, str)
        self.assertIn("LinkedIn", prompt.lower())
        self.assertIn("business", prompt.lower())
    
    def test_generate_negative_prompt(self):
        """Test negative prompt generation."""
        negative_prompt = self.generator.generate_negative_prompt()
        self.assertIsInstance(negative_prompt, str)
        self.assertIn("blurry", negative_prompt)

if __name__ == '__main__':
    unittest.main()
