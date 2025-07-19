"""
Advanced prompt generation for Flux AI models.
"""

from typing import Dict, Any

class PromptGenerator:
    """Generates optimized prompts for Flux AI portrait generation."""
    
    def __init__(self):
        self.purpose_details = {
            "LinkedIn": "professional headshot optimized for social media",
            "Resume": "formal professional portrait for career applications",
            "Corporate Website": "executive-level corporate portrait",
            "Personal Branding": "distinctive personal brand portrait",
            "Business Card": "compact professional headshot",
            "Other": "professional portrait"
        }
        
        self.attire_details = {
            "Business Formal": "sharp business suit, professional tie, polished appearance",
            "Business Casual": "smart blazer, dress shirt, refined casual look",
            "Smart Casual": "stylish casual wear, modern professional appearance",
            "Creative Professional": "fashionable, artistic professional attire",
            "Academic": "scholarly attire, professional academic dress",
            "Other": "appropriate professional clothing"
        }
        
        self.background_details = {
            "Corporate Office": "modern office environment, soft bokeh, professional lighting",
            "Plain Color": "clean gradient background, studio lighting",
            "Outdoor": "natural outdoor setting, soft natural lighting",
            "Studio-like": "professional studio setup, controlled lighting",
            "Library/Academic": "scholarly environment, books, academic setting",
            "Creative Space": "artistic workspace, creative elements, modern aesthetic",
            "Other": "appropriate professional background"
        }
        
        self.vibe_details = {
            "Confident": "confident expression, direct gaze, strong posture",
            "Friendly": "warm smile, approachable demeanor, friendly eyes",
            "Approachable": "gentle smile, open expression, welcoming appearance",
            "Authoritative": "commanding presence, serious expression, leadership aura",
            "Creative": "artistic expression, creative energy, innovative look",
            "Sophisticated": "refined elegance, intellectual appearance, polished style",
            "Warm": "genuine warmth, kind expression, compassionate presence"
        }
        
        self.lighting_details = {
            "Natural Light": "soft natural lighting, window light",
            "Studio Lighting": "professional studio lighting setup",
            "Soft Lighting": "gentle, diffused lighting",
            "Dramatic Lighting": "dramatic shadows and highlights",
            "Golden Hour": "warm golden hour lighting",
            "Professional Flash": "professional flash photography lighting"
        }
        
        self.mood_details = {
            "Professional": "professional demeanor",
            "Casual": "relaxed, casual atmosphere",
            "Serious": "serious, focused expression",
            "Energetic": "dynamic, energetic presence",
            "Calm": "calm, peaceful demeanor",
            "Inspiring": "inspiring, motivational presence"
        }
    
    def generate_prompt(self, profile_data: Dict[str, Any]) -> str:
        """Generate an advanced Flux prompt based on profile data."""
        
        # Extract basic info
        purpose = profile_data.get('purpose', '')
        attire = profile_data.get('attire', '')
        background = profile_data.get('background', '')
        vibe = profile_data.get('vibe', '')
        
        # Extract advanced settings
        lighting = profile_data.get('lighting', 'Professional Flash')
        mood = profile_data.get('mood', 'Professional')
        custom_notes = profile_data.get('custom_notes', '')
        
        # Build detailed descriptions
        purpose_desc = self.purpose_details.get(purpose, 'professional portrait')
        attire_desc = self.attire_details.get(attire, 'professional attire')
        background_desc = self.background_details.get(background, 'professional background')
        vibe_desc = self.vibe_details.get(vibe, 'professional demeanor')
        lighting_desc = self.lighting_details.get(lighting, 'professional lighting')
        mood_desc = self.mood_details.get(mood, 'professional demeanor')
        
        # Construct the main prompt
        prompt = (
            f"Ultra-realistic {purpose_desc}, featuring {attire_desc}, "
            f"set against {background_desc}, with {vibe_desc}, "
            f"{lighting_desc}, {mood_desc}, "
            f"professional photography, high resolution, cinematic lighting, "
            f"sharp focus, professional color grading, detailed facial features"
        )
        
        # Add custom notes if provided
        if custom_notes and custom_notes.strip():
            prompt += f", {custom_notes.strip()}"
        
        # Add quality modifiers
        prompt += ", masterpiece, best quality, highly detailed, photorealistic"
        
        return prompt
    
    def generate_negative_prompt(self) -> str:
        """Generate a negative prompt to avoid unwanted elements."""
        return (
            "blurry, low quality, pixelated, distorted, ugly, deformed, "
            "bad anatomy, bad proportions, extra limbs, mutation, "
            "low resolution, jpeg artifacts, watermark, signature, "
            "cartoon, anime, painting, illustration, 3d render"
        )
