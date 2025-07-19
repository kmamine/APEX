"""
APEX: Agentic Portrait EXperience - User Preferences Form

This module creates a Gradio interface for collecting user preferences for professional portrait generation.
It allows users to specify purpose, attire, background, vibe, and optionally upload a reference photo.
The collected preferences are structured into JSON format for further processing.
"""

import gradio as gr
import json
import os
from datetime import datetime
from typing import Optional, Dict, Any, List
import base64

def validate_inputs(purpose: str, attire: str, background: str, vibe: str) -> tuple[bool, str]:
    """Validate user inputs and return validation status and message."""
    if not purpose:
        return False, "⚠️ Please select a purpose for your portrait"
    if not attire:
        return False, "⚠️ Please select your preferred attire"
    if not background:
        return False, "⚠️ Please select a background style"
    if not vibe:
        return False, "⚠️ Please select your desired vibe"
    return True, "✅ All inputs valid"

def save_profile_to_file(profile: Dict[str, Any], filename: str = None) -> str:
    """Save the profile to a JSON file."""
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portrait_profile_{timestamp}.json"
    
    # Create profiles directory if it doesn't exist
    os.makedirs("profiles", exist_ok=True)
    filepath = os.path.join("profiles", filename)
    
    with open(filepath, 'w') as f:
        json.dump(profile, f, indent=2)
    
    return filepath

def load_profile_presets() -> Dict[str, Dict[str, str]]:
    """Load predefined profile presets for quick selection."""
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

def generate_advanced_prompt(profile: Dict[str, Any]) -> str:
    """Generate an advanced Flux prompt based on the profile."""
    
    # Mapping for more detailed descriptions
    purpose_details = {
        "LinkedIn": "professional headshot optimized for social media",
        "Resume": "formal professional portrait for career applications",
        "Corporate Website": "executive-level corporate portrait",
        "Personal Branding": "distinctive personal brand portrait",
        "Business Card": "compact professional headshot",
        "Other": "professional portrait"
    }
    
    attire_details = {
        "Business Formal": "sharp business suit, professional tie, polished appearance",
        "Business Casual": "smart blazer, dress shirt, refined casual look",
        "Smart Casual": "stylish casual wear, modern professional appearance",
        "Creative Professional": "fashionable, artistic professional attire",
        "Academic": "scholarly attire, professional academic dress",
        "Other": "appropriate professional clothing"
    }
    
    background_details = {
        "Corporate Office": "modern office environment, soft bokeh, professional lighting",
        "Plain Color": "clean gradient background, studio lighting",
        "Outdoor": "natural outdoor setting, soft natural lighting",
        "Studio-like": "professional studio setup, controlled lighting",
        "Library/Academic": "scholarly environment, books, academic setting",
        "Creative Space": "artistic workspace, creative elements, modern aesthetic",
        "Other": "appropriate professional background"
    }
    
    vibe_details = {
        "Confident": "confident expression, direct gaze, strong posture",
        "Friendly": "warm smile, approachable demeanor, friendly eyes",
        "Approachable": "gentle smile, open expression, welcoming appearance",
        "Authoritative": "commanding presence, serious expression, leadership aura",
        "Creative": "artistic expression, creative energy, innovative look",
        "Sophisticated": "refined elegance, intellectual appearance, polished style",
        "Warm": "genuine warmth, kind expression, compassionate presence"
    }
    
    # Build the prompt
    purpose_desc = purpose_details.get(profile['purpose'], 'professional portrait')
    attire_desc = attire_details.get(profile['attire'], 'professional attire')
    background_desc = background_details.get(profile['background'], 'professional background')
    vibe_desc = vibe_details.get(profile['vibe'], 'professional demeanor')
    
    prompt = f"""Ultra-realistic {purpose_desc}, featuring {attire_desc}, set against {background_desc}, with {vibe_desc}, professional photography, high resolution, cinematic lighting, sharp focus, professional color grading"""
    
    if profile.get('custom_notes'):
        prompt += f", {profile['custom_notes']}"
    
    return prompt

def collect_user_preferences(purpose: str, attire: str, background: str, vibe: str, 
                           photo: Optional[str], custom_notes: str, lighting: str, 
                           mood: str, age_range: str, gender: str, ethnicity: str,
                           resolution: str, save_profile: bool, preset_name: str = None) -> tuple[str, str, str, str]:
    """
    Collect and validate user preferences, then create a comprehensive style profile.
    
    Returns:
        tuple: (JSON profile string, status message, advanced prompt, saved file path)
    """
    # Validate inputs
    is_valid, message = validate_inputs(purpose, attire, background, vibe)
    if not is_valid:
        return "", message, "", ""
    
    # Create a comprehensive style profile
    profile = {
        "basic_info": {
            "purpose": purpose,
            "attire": attire,
            "background": background,
            "vibe": vibe
        },
        "advanced_settings": {
            "lighting": lighting,
            "mood": mood,
            "age_range": age_range,
            "gender": gender,
            "ethnicity": ethnicity,
            "resolution": resolution
        },
        "additional_info": {
            "reference_photo": "uploaded" if photo else None,
            "custom_notes": custom_notes.strip() if custom_notes else None,
            "preset_used": preset_name if preset_name else None
        },
        "metadata": {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "version": "2.0",
            "created_by": "APEX Portrait Generator"
        }
    }
    
    # Generate advanced prompt
    advanced_prompt = generate_advanced_prompt({
        'purpose': purpose,
        'attire': attire,
        'background': background,
        'vibe': vibe,
        'custom_notes': custom_notes,
        'lighting': lighting,
        'mood': mood
    })
    
    profile["generated_prompt"] = advanced_prompt
    
    # Save to file if requested
    saved_file = ""
    if save_profile:
        try:
            saved_file = save_profile_to_file(profile)
            save_message = f" | 💾 Saved to: {saved_file}"
        except Exception as e:
            save_message = f" | ⚠️ Save failed: {str(e)}"
    else:
        save_message = ""
    
    json_output = json.dumps(profile, indent=2)
    success_message = f"✅ Advanced style profile generated successfully!{save_message}"
    
    return json_output, success_message, advanced_prompt, saved_file

def apply_preset(preset_name: str) -> tuple[str, str, str, str, str]:
    """Apply a preset configuration."""
    presets = load_profile_presets()
    if preset_name and preset_name in presets:
        preset = presets[preset_name]
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
                    choices=list(load_profile_presets().keys()),
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
            fn=collect_user_preferences,
            inputs=[purpose, attire, background, vibe, photo, custom_notes, 
                   lighting, mood, age_range, gender, ethnicity, resolution, save_profile],
            outputs=[output, status, advanced_prompt, saved_file]
        )
        
        apply_preset_btn.click(
            fn=apply_preset,
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

if __name__ == "__main__":
    # Create and launch the enhanced interface
    demo = create_interface()
    demo.launch(
        share=True,  # Enable sharing for easier access
        inbrowser=True,
        show_error=True,
        server_name="127.0.0.1",
        server_port=7860,
        favicon_path=None,  # You can add a custom favicon
        app_kwargs={"docs_url": "/docs", "redoc_url": "/redoc"}  # Enable API docs
    )       