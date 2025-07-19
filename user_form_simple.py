"""
APEX: Agentic Portrait EXperience - Simple User Preferences Form

This module creates a simple, compatible Gradio interface for collecting user preferences.
"""

import gradio as gr
import json
from datetime import datetime

def collect_user_preferences(purpose, attire, background, vibe, photo, custom_notes):
    """Collect user preferences and create a structured style profile."""
    
    # Validate required inputs
    if not purpose:
        return "", "⚠️ Please select a purpose for your portrait"
    if not attire:
        return "", "⚠️ Please select your preferred attire"
    if not background:
        return "", "⚠️ Please select a background style"
    if not vibe:
        return "", "⚠️ Please select your desired vibe"
    
    # Create the profile
    profile = {
        "purpose": purpose,
        "attire": attire,
        "background": background,
        "vibe": vibe,
        "reference_photo": "uploaded" if photo else None,
        "custom_notes": custom_notes.strip() if custom_notes else None,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    json_output = json.dumps(profile, indent=2)
    success_message = "✅ Style profile generated successfully! Ready for portrait generation."
    
    return json_output, success_message

def clear_form():
    """Clear all form fields."""
    return "", "", "", "", None, "", "", "🔄 Form cleared! Ready for new input."

# Create the interface
with gr.Blocks(title="APEX Portrait Generator") as demo:
    gr.Markdown("""
    # 🖼️ **APEX: Agentic Portrait EXperience**
    ## Professional Portrait Preferences Form
    Fill out your preferences below to generate your perfect professional portrait.
    """)
    
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
    
    with gr.Row():
        photo = gr.Image(
            label="📸 Optional reference photo", 
            type="filepath"
        )
        custom_notes = gr.Textbox(
            label="📝 Additional notes",
            placeholder="Any specific requests... (e.g., 'prefer natural lighting', 'avoid busy backgrounds')",
            lines=3
        )
    
    with gr.Row():
        submit_btn = gr.Button("✅ Generate Style Profile", variant="primary")
        clear_btn = gr.Button("🔄 Clear Form")
    
    with gr.Row():
        with gr.Column():
            output = gr.Textbox(
                label="Generated Style Profile (JSON)", 
                lines=10
            )
        with gr.Column():
            status = gr.Textbox(
                label="Status",
                lines=3
            )
    
    # Event handlers
    submit_btn.click(
        fn=collect_user_preferences,
        inputs=[purpose, attire, background, vibe, photo, custom_notes],
        outputs=[output, status]
    )
    
    clear_btn.click(
        fn=clear_form,
        outputs=[purpose, attire, background, vibe, photo, custom_notes, output, status]
    )
    
    gr.Markdown("""
    ### 💡 **Example Use Cases:**
    - **LinkedIn Professional**: Business Formal + Corporate Office + Confident
    - **Creative Portfolio**: Creative Professional + Studio-like + Creative  
    - **Academic Profile**: Business Casual + Library/Academic + Sophisticated
    - **Startup Founder**: Smart Casual + Creative Space + Approachable
    """)

if __name__ == "__main__":
    demo.launch(
        share=True,  # This creates a public link that's accessible
        inbrowser=True,
        show_error=True
    )
