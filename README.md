# 🖼️ **APEX: Agentic Portrait EXperience**

**APEX** is an **agentic, iterative portrait generation system** that uses **LLMs, VLMs, and Flux diffusion models** to create **high-quality professional portraits**. It mimics a **human photographer's workflow**, refining each generation step until the result perfectly matches the user's desired style, attire, vibe, and background.

## 📋 **Table of Contents**
- [System Architecture](#-system-architecture)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Usage Examples](#-usage-examples)
- [Contributing](#-contributing)️ **APEX: Agentic Portrait EXperience**

**APEX** is an **agentic, iterative portrait generation system** that uses **LLMs, VLMs, and Flux diffusion models** to create **high-quality professional portraits**.
It mimics a **human photographer’s workflow**, refining each generation step until the result perfectly matches the user’s desired style, attire, vibe, and background.

## 🏗️ **System Architecture**

```
[User Form Input]
        ↓
[LLM Style Planner] → Generates structured style profile + Flux prompt
        ↓
[Flux Generation] → Creates initial portrait
        ↓
[VLM Judge + Scoring] → Evaluates style, vibe, background, aesthetics
        ↓
[LLM Prompt Refiner] → Improves prompt based on feedback
        ↓
(loop until quality threshold reached)
        ↓
[Post-Processing] → Final polished portrait
```

---

## ✨ **Key Features**

✅ **Interactive User Form** – Collects purpose, attire, vibe, and background preferences
✅ **LLM Style Planner** – Transforms user preferences into a **structured style profile & Flux prompt**
✅ **Flux Portrait Generation** – Creates **photorealistic professional portraits**
✅ **Iterative Feedback Loop** – Uses a **Vision-Language Judge (VLM)** to evaluate results and **refine prompts**
✅ **Style & Quality Scoring** – Ensures the portrait meets the requested style with **quantitative evaluation**
✅ **Identity Preservation (optional)** – Upload a reference photo for **InstantID/IP-Adapter** support
✅ **Post-Processing** – Face enhancement, background cleanup, and high-resolution upscaling

---

## 🧠 **How It Works**

1. **User Inputs Preferences**  
   - Example: *“I need a LinkedIn portrait in formal attire, corporate background, confident & approachable vibe.”*

2. **LLM Reasoning (Style Planner)**  
   - Generates a **Flux prompt**:  
     > *“Ultra-realistic LinkedIn headshot, navy blue business suit, bright soft lighting, blurred corporate office background, confident approachable smile, cinematic depth of field.”*

3. **Flux Generation**  
   - Creates the **first portrait**

4. **VLM Judge + Scoring**  
   - Checks: Does attire match? Does background fit? Is the vibe correct?  
   - Gives **feedback + scores**

5. **Prompt Refinement**  
   - LLM refines the prompt → regenerates portrait → repeats until **high-scoring result**

6. **Final Polishing**  
   - Optional face enhancement, background cleanup, and upscale

---

## 🚀 **Installation**

### Prerequisites
- Python 3.8+
- CUDA-capable GPU (recommended)
- 8GB+ VRAM for optimal performance

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/apex-portrait.git
   cd apex-portrait
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Required Dependencies
- `gradio` - Frontend UI
- `transformers` - LLM + VLM models
- `diffusers` - Flux/SDXL generation
- `torch` - PyTorch backend
- `clip-by-openai` - CLIP scoring
- `aesthetic-score` - Quality assessment

---

## ⚡ **Quick Start**

1. **Launch the application**
   ```bash
   python app.py
   ```
   
   Or use the legacy standalone form:
   ```bash
   python user_form.py
   ```

2. **Access the web interface**
   - Open your browser and go to `http://127.0.0.1:7860`

3. **Fill out your preferences**
   - Select your portrait purpose (LinkedIn, Professional, etc.)
   - Choose attire style, background, and vibe
   - Configure advanced settings (lighting, mood, demographics)
   - Optionally upload a reference photo

4. **Generate your profile**
   - The system will create a comprehensive JSON profile
   - Get an optimized Flux prompt for AI generation
   - Profiles are automatically saved for future use

### Package Usage Example
```python
from apex import ProfileManager, PromptGenerator

# Create managers
profile_manager = ProfileManager()
prompt_generator = PromptGenerator()

# Create a profile
profile, is_valid, message = profile_manager.create_profile(
    purpose="LinkedIn",
    attire="Business Formal", 
    background="Corporate Office",
    vibe="Confident"
)

# Generate prompt
prompt_data = profile.to_dict()
flux_prompt = prompt_generator.generate_prompt(prompt_data)
```

---

## 📁 **Project Structure**

```
APEX/
├── README.md                    # Project documentation
├── requirements.txt             # Dependencies
├── app.py                      # Main application entry point
├── user_form.py                # Legacy standalone form (deprecated)
├── user_form_simple.py         # Simple standalone form (deprecated)
├── apex/                       # Main package
│   ├── __init__.py
│   ├── config/                 # Configuration management
│   │   ├── __init__.py
│   │   └── settings.py         # Application settings
│   ├── core/                   # Core business logic
│   │   ├── __init__.py
│   │   ├── profile_manager.py  # Profile management and file operations
│   │   └── prompt_generator.py # AI prompt generation
│   ├── models/                 # Data models
│   │   ├── __init__.py
│   │   └── profile.py          # Profile data structures
│   ├── ui/                     # User interface
│   │   ├── __init__.py
│   │   └── gradio_interface.py # Gradio web interface
│   └── utils/                  # Utility functions
│       ├── __init__.py
│       ├── file_utils.py       # File operations
│       └── validators.py       # Data validation
├── data/                       # Data storage
│   ├── profiles/               # Saved user profiles
│   └── uploads/                # Uploaded reference images
└── tests/                      # Test suite
    ├── __init__.py
    └── test_basic.py           # Basic functionality tests
```

---

## 💡 **Usage Examples**

### LinkedIn Professional Portrait
```python
from agentic_loop import APEXGenerator

generator = APEXGenerator()
result = generator.generate({
    "purpose": "LinkedIn",
    "attire": "Business Formal",
    "background": "Corporate Office",
    "vibe": "Confident & Approachable"
})
```

### Creative Portrait
```python
result = generator.generate({
    "purpose": "Creative Portfolio",
    "attire": "Artistic Casual",
    "background": "Studio",
    "vibe": "Creative & Innovative"
})
```

---

## 🤝 **Contributing**

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- Flux AI for the diffusion models
- Hugging Face for the transformer models
- The open-source AI community for inspiration and tools

---

**Made with ❤️ for creating perfect professional portraits**