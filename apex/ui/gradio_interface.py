"""
Gradio user interface for APEX portrait generation.
"""

import gradio as gr
from typing import Optional, Tuple
from ..core.profile_manager import ProfileManager
from ..core.prompt_generator import PromptGenerator

class APEXInterface:
    """Main interface class for APEX portrait generation."""
    
    def __init__(self):
        self.profile_manager = ProfileManager()
        self.prompt_generator = PromptGenerator()
    
    def collect_user_preferences(self, purpose: str, attire: str, background: str, vibe: str, 
                               photo: Optional[str], custom_notes: str, lighting: str, 
                               mood: str, age_range: str, gender: str, ethnicity: str,
                               resolution: str, save_profile: bool, preset_name: str = None) -> Tuple[str, str, str, str]:
        """
        Collect and validate user preferences, then create a comprehensive style profile.
        
        Returns:
            tuple: (JSON profile string, status message, advanced prompt, saved file path)
        """
        # Create profile using ProfileManager
        profile_data, is_valid, message = self.profile_manager.create_profile(
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
            photo_path=photo,
            custom_notes=custom_notes,
            preset_name=preset_name
        )
        
        if not is_valid:
            return "", message, "", ""
        
        # Generate advanced prompt
        prompt_data = {
            'purpose': purpose,
            'attire': attire,
            'background': background,
            'vibe': vibe,
            'lighting': lighting,
            'mood': mood,
            'custom_notes': custom_notes
        }
        advanced_prompt = self.prompt_generator.generate_prompt(prompt_data)
        profile_data.generated_prompt = advanced_prompt
        
        # Save to file if requested
        saved_file = ""
        if save_profile:
            try:
                saved_file = self.profile_manager.save_profile(profile_data)
                save_message = f" | 💾 Saved to: {saved_file}"
            except Exception as e:
                save_message = f" | ⚠️ Save failed: {str(e)}"
        else:
            save_message = ""
        
        # Generate outputs
        import json
        json_output = json.dumps(profile_data.to_dict(), indent=2)
        success_message = f"✅ Advanced style profile generated successfully!{save_message}"
        
        return json_output, success_message, advanced_prompt, saved_file
    
    def apply_preset(self, preset_name: str) -> Tuple[str, str, str, str, str]:
        """Apply a preset configuration."""
        preset = self.profile_manager.apply_preset(preset_name)
        if preset:
            return (
                preset["purpose"],
                preset["attire"], 
                preset["background"],
                preset["vibe"],
                preset["custom_notes"]
            )
        return "", "", "", "", ""

def create_interface() -> gr.Blocks:
    """Create and configure the Gradio interface."""
    
    interface = APEXInterface()
    
    # Custom CSS for better styling
    css = """
    .container {
        max-width: 1200px;
        margin: auto;
    }
    .title {
        text-align: center;
        color: #2D5AA0;
        margin-bottom: 20px;
    }
    .preset-section {
        background: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .advanced-section {
        background: #e8f4f8;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }
    .output-section {
        background: #fff;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ddd;
    }
    """
    
    with gr.Blocks(css=css, title="APEX Portrait Generator") as demo:
        gr.Markdown(
            "# 🖼️ **APEX: Agentic Portrait EXperience**\n"
            "## Advanced Professional Portrait Preferences Form\n"
            "Create detailed style profiles for AI-generated professional portraits with advanced customization options.",
            elem_classes="title"
        )
        
        # Preset Selection Section
        with gr.Group(elem_classes="preset-section"):
            gr.Markdown("### 🎯 **Quick Start Presets**")
            with gr.Row():
                preset_dropdown = gr.Dropdown(
                    choices=list(interface.profile_manager.get_presets().keys()),
                    label="📋 Choose a preset",
                    value=None
                )
                apply_preset_btn = gr.Button("✨ Apply Preset", variant="secondary", size="sm")
        
        # Basic Settings Section
        gr.Markdown("### 🔧 **Basic Settings**")
        with gr.Row():
            with gr.Column():
                purpose = gr.Dropdown(
                    choices=["LinkedIn", "Resume", "Corporate Website", "Personal Branding", "Business Card", "Other"],
                    label="📌 What is the portrait for?"
                )
                attire = gr.Dropdown(
                    choices=["Business Formal", "Business Casual", "Smart Casual", "Creative Professional", "Academic", "Other"],
                    label="👔 Preferred attire"
                )
            
            with gr.Column():
                background = gr.Dropdown(
                    choices=["Corporate Office", "Plain Color", "Outdoor", "Studio-like", "Library/Academic", "Creative Space", "Other"],
                    label="🏢 Background style"
                )
                vibe = gr.Dropdown(
                    choices=["Confident", "Friendly", "Approachable", "Authoritative", "Creative", "Sophisticated", "Warm"],
                    label="😊 Desired vibe"
                )
        
        # Advanced Settings Section
        with gr.Group(elem_classes="advanced-section"):
            gr.Markdown("### ⚙️ **Advanced Settings**")
            with gr.Row():
                with gr.Column():
                    lighting = gr.Dropdown(
                        choices=["Natural Light", "Studio Lighting", "Soft Lighting", "Dramatic Lighting", "Golden Hour", "Professional Flash"],
                        label="💡 Lighting Style",
                        value="Professional Flash"
                    )
                    mood = gr.Dropdown(
                        choices=["Professional", "Casual", "Serious", "Energetic", "Calm", "Inspiring"],
                        label="🎭 Overall Mood",
                        value="Professional"
                    )
                    resolution = gr.Dropdown(
                        choices=["1024x1024 (Standard)", "1536x1024 (Wide)", "1024x1536 (Portrait)", "2048x2048 (High-Res)"],
                        label="📐 Resolution",
                        value="1024x1024 (Standard)"
                    )
                
                with gr.Column():
                    age_range = gr.Dropdown(
                        choices=["20-30", "30-40", "40-50", "50-60", "60+", "Not Specified"],
                        label="🎂 Age Range",
                        value="Not Specified"
                    )
                    gender = gr.Dropdown(
                        choices=["Male", "Female", "Non-binary", "Not Specified"],
                        label="👤 Gender",
                        value="Not Specified"
                    )
                    ethnicity = gr.Dropdown(
                        choices=["Asian", "Black", "Caucasian", "Hispanic", "Middle Eastern", "Mixed", "Not Specified"],
                        label="🌍 Ethnicity",
                        value="Not Specified"
                    )
        
        # Upload and Notes Section
        with gr.Row():
            photo = gr.Image(
                label="📸 Optional reference photo", 
                type="filepath"
            )
            custom_notes = gr.Textbox(
                label="📝 Additional notes & specific requirements",
                placeholder="Describe any specific details: facial hair, glasses, jewelry, specific poses, lighting preferences, etc.",
                lines=5
            )
        
        # Options and Controls
        with gr.Row():
            with gr.Column():
                save_profile = gr.Checkbox(
                    label="💾 Save profile to file",
                    value=True
                )
            with gr.Column():
                submit_btn = gr.Button("🚀 Generate Advanced Profile", variant="primary", size="lg")
                clear_btn = gr.Button("🔄 Clear All Fields", variant="secondary")
        
        # Output Section
        gr.Markdown("### 📋 **Generated Outputs**")
        with gr.Group(elem_classes="output-section"):
            with gr.Row():
                with gr.Column():
                    output = gr.Textbox(
                        label="📄 Complete Style Profile (JSON)", 
                        lines=15,
                        max_lines=20
                    )
                with gr.Column():
                    advanced_prompt = gr.Textbox(
                        label="🎨 Generated Flux Prompt",
                        lines=8,
                        max_lines=12
                    )
            
            with gr.Row():
                with gr.Column():
                    status = gr.Textbox(
                        label="📊 Status & Information",
                        lines=3
                    )
                with gr.Column():
                    saved_file = gr.Textbox(
                        label="💾 Saved File Path",
                        lines=2
                    )
        
        # Event handlers
        submit_btn.click(
            fn=interface.collect_user_preferences,
            inputs=[purpose, attire, background, vibe, photo, custom_notes, 
                   lighting, mood, age_range, gender, ethnicity, resolution, save_profile],
            outputs=[output, status, advanced_prompt, saved_file]
        )
        
        apply_preset_btn.click(
            fn=interface.apply_preset,
            inputs=[preset_dropdown],
            outputs=[purpose, attire, background, vibe, custom_notes]
        )
        
        clear_btn.click(
            fn=lambda: ("", "", "", "", None, "", "", "", "", "", "", "", False, "", "", "", ""),
            outputs=[purpose, attire, background, vibe, photo, custom_notes, 
                    lighting, mood, age_range, gender, ethnicity, resolution, save_profile,
                    output, status, advanced_prompt, saved_file]
        )
        
        # Enhanced Example section with tips
        gr.Markdown("""
        ### 💡 **Example Use Cases & Tips**
        
        **Quick Presets:**
        - **LinkedIn Professional**: Perfect for professional networking and career profiles
        - **Creative Portfolio**: Ideal for artists, designers, and creative professionals  
        - **Academic Profile**: Great for researchers, professors, and academic professionals
        - **Startup Founder**: Modern look for entrepreneurs and startup leaders
        - **Executive Portrait**: High-level corporate portraits for C-suite executives
        
        **Pro Tips:**
        - 📸 **Reference Photos**: Upload a clear headshot for better style matching
        - 💡 **Lighting**: "Natural Light" for warmth, "Studio Lighting" for crispness
        - 🎭 **Mood**: Match the mood to your industry and personal brand
        - 📐 **Resolution**: Use "Portrait" for vertical layouts, "Wide" for headers
        - 📝 **Custom Notes**: Be specific about glasses, facial hair, jewelry, etc.
        
        **Advanced Features:**
        - ✨ **Preset System**: Quick-start templates for common scenarios
        - 💾 **Profile Saving**: Automatically saves configurations for future use
        - 🎨 **Smart Prompts**: AI-generated prompts optimized for Flux models
        - 📊 **Detailed Metadata**: Complete tracking and version information
        """)
    
    return demo
