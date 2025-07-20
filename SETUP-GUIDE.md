# 🖼️ APEX Portrait Generator - Complete Setup Guide

A comprehensive guide for setting up the APEX Portrait Generator on any machine, including both the Python backend and React web frontend.

## 📋 Table of Contents

- [🎯 Quick Start](#-quick-start)
- [📦 Prerequisites](#-prerequisites)
- [🐍 Python Backend Setup](#-python-backend-setup)
- [⚛️ React Web App Setup](#️-react-web-app-setup)
- [🖥️ Platform-Specific Instructions](#️-platform-specific-instructions)
- [🔧 Troubleshooting](#-troubleshooting)
- [📱 Usage Guide](#-usage-guide)
- [🤝 Contributing](#-contributing)

---

## 🎯 Quick Start

### For Web App Only (Recommended for most users):
```bash
git clone https://github.com/kmamine/FluxPortrait.git
cd FluxPortrait/web-app
./setup.sh
```

### For Full System (Python + Web):
```bash
git clone https://github.com/kmamine/FluxPortrait.git
cd FluxPortrait

# Setup Python backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Setup React frontend
cd web-app
./setup.sh
```

---

## 📦 Prerequisites

### Essential Requirements

| Component | Version | Purpose | Installation |
|-----------|---------|---------|-------------|
| **Node.js** | 18+ | Web app development | [nodejs.org](https://nodejs.org/) |
| **Python** | 3.8+ | Backend processing | [python.org](https://python.org/) |
| **Git** | 2.0+ | Version control | [git-scm.com](https://git-scm.com/) |

### System Requirements

- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space
- **Network**: Internet connection for package installation
- **OS**: macOS, Windows 10+, or Linux

---

## 🐍 Python Backend Setup

The Python backend handles the AI processing and core functionality.

### Step 1: Clone Repository
```bash
git clone https://github.com/kmamine/FluxPortrait.git
cd FluxPortrait
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Verify activation (should show (venv) in prompt)
which python  # Should point to venv/bin/python
```

### Step 3: Install Python Dependencies
```bash
# Install minimal requirements (faster)
pip install -r requirements-minimal.txt

# OR install full requirements (includes all optional packages)
pip install -r requirements.txt

# Verify installation
python -c "import apex; print('APEX installed successfully')"
```

### Step 4: Test Python Backend
```bash
# Test the basic functionality
python app.py

# Or test with the simple form
python user_form_simple.py
```

### Python Package Overview
```
Core Dependencies:
├── gradio              # Web interface framework
├── transformers        # AI model handling
├── torch              # Machine learning backend
├── pillow             # Image processing
├── requests           # HTTP requests
└── json               # Data serialization

Optional Dependencies:
├── accelerate         # Model acceleration
├── diffusers          # Diffusion models
├── xformers           # Memory optimization
└── safetensors        # Secure model loading
```

---

## ⚛️ React Web App Setup

The React web app provides a modern, responsive interface.

### Step 1: Navigate to Web App
```bash
cd FluxPortrait/web-app
```

### Step 2: Check System Requirements
```bash
# Run our requirements checker
./check-requirements.sh

# Or manually check:
node --version    # Should be 18+
npm --version     # Should be 8+
```

### Step 3: Automated Setup
```bash
# Make setup script executable (if needed)
chmod +x setup.sh

# Run automated setup
./setup.sh
```

### Step 4: Manual Setup (Alternative)
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production (optional)
npm run build
```

### React Dependencies Overview
```
Core Dependencies:
├── react@18           # UI framework
├── react-dom@18       # DOM rendering
├── typescript         # Type safety
├── vite              # Build tool
└── tailwindcss       # Styling framework

Development Dependencies:
├── @vitejs/plugin-react    # React integration
├── eslint                  # Code linting
├── @types/react           # TypeScript definitions
└── postcss               # CSS processing
```

---

## 🖥️ Platform-Specific Instructions

### 🍎 macOS Setup

#### Install Prerequisites
```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add Homebrew to PATH
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# Install Node.js and Python
brew install node python

# Verify installations
node --version && python3 --version
```

#### Complete Setup
```bash
# Clone and setup
git clone https://github.com/kmamine/FluxPortrait.git
cd FluxPortrait

# Python setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# React setup
cd web-app
./setup.sh
```

### 🪟 Windows Setup

#### Install Prerequisites
```powershell
# Option 1: Using Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
choco install nodejs python git

# Option 2: Manual installation
# Download from:
# - Node.js: https://nodejs.org/
# - Python: https://python.org/
# - Git: https://git-scm.com/
```

#### Complete Setup
```bash
# Clone and setup
git clone https://github.com/kmamine/FluxPortrait.git
cd FluxPortrait

# Python setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# React setup
cd web-app
npm install
npm run dev
```

### 🐧 Linux Setup

#### Install Prerequisites
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nodejs npm python3 python3-pip python3-venv git

# CentOS/RHEL/Fedora
sudo dnf install nodejs npm python3 python3-pip git

# Arch Linux
sudo pacman -S nodejs npm python python-pip git

# Verify installations
node --version && python3 --version
```

#### Complete Setup
```bash
# Clone and setup
git clone https://github.com/kmamine/FluxPortrait.git
cd FluxPortrait

# Python setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# React setup
cd web-app
chmod +x setup.sh
./setup.sh
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 🐍 Python Issues

**"Python not found"**
```bash
# Check if Python is installed
python --version || python3 --version

# Install Python
# macOS: brew install python
# Windows: Download from python.org
# Linux: sudo apt install python3
```

**"pip not found"**
```bash
# Install pip
python -m ensurepip --upgrade
# Or: curl https://bootstrap.pypa.io/get-pip.py | python
```

**"Virtual environment activation fails"**
```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv

# Activate with correct path
# macOS/Linux: source venv/bin/activate
# Windows: venv\Scripts\activate
```

**"Package installation fails"**
```bash
# Upgrade pip first
pip install --upgrade pip

# Clear cache and retry
pip cache purge
pip install -r requirements.txt

# Install packages individually if needed
pip install gradio transformers torch pillow
```

#### ⚛️ React/Node.js Issues

**"Node.js not found"**
```bash
# Install Node.js
# macOS: brew install node
# Windows: choco install nodejs
# Linux: sudo apt install nodejs npm

# Verify installation
node --version && npm --version
```

**"npm install fails"**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and retry
rm -rf node_modules package-lock.json
npm install

# Try with different registry
npm install --registry https://registry.npmjs.org/
```

**"Port 3000 already in use"**
```bash
# Find and kill process using port 3000
# macOS/Linux:
lsof -ti:3000 | xargs kill -9

# Windows:
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# Use different port
npm run dev -- --port 3001
```

**"Permission denied on setup.sh"**
```bash
# Make script executable
chmod +x setup.sh

# Or run manually
npm install && npm run dev
```

#### 🔗 Network Issues

**"Connection timeout during installation"**
```bash
# Try with different DNS
# macOS/Linux: Add to /etc/resolv.conf
nameserver 8.8.8.8
nameserver 8.8.4.4

# Use corporate proxy (if applicable)
npm config set proxy http://proxy.company.com:8080
npm config set https-proxy http://proxy.company.com:8080
```

**"SSL certificate errors"**
```bash
# Disable SSL verification (temporary fix)
npm config set strict-ssl false
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# Better: Update certificates
# macOS: brew upgrade ca-certificates
# Windows: Update Windows
# Linux: sudo apt update && sudo apt upgrade ca-certificates
```

#### 💾 Storage Issues

**"No space left on device"**
```bash
# Check disk space
df -h

# Clean npm cache
npm cache clean --force

# Clean pip cache
pip cache purge

# Remove old node_modules
find . -name "node_modules" -type d -exec rm -rf {} +
```

---

## 📱 Usage Guide

### Starting the Applications

#### Option 1: Web App Only (Recommended)
```bash
cd FluxPortrait/web-app
npm run dev
# Access at: http://localhost:3000
```

#### Option 2: Python Backend Only
```bash
cd FluxPortrait
source venv/bin/activate  # Windows: venv\Scripts\activate
python app.py
# Access at: http://localhost:7860
```

#### Option 3: Both Applications
```bash
# Terminal 1 - Python Backend
cd FluxPortrait
source venv/bin/activate
python app.py

# Terminal 2 - React Frontend
cd FluxPortrait/web-app
npm run dev
```

### Feature Comparison

| Feature | Python Backend | React Web App |
|---------|----------------|---------------|
| **Interface** | Gradio-based | Modern React |
| **Mobile Support** | Basic | Fully responsive |
| **Performance** | Good | Excellent |
| **Customization** | Limited | Highly customizable |
| **AI Processing** | Full integration | JSON export only |
| **Offline Usage** | Yes | Yes (after build) |

### Using the Web App

1. **Select a Preset**: Choose from 5 professional templates
2. **Fill Form**: Complete the profile information
3. **Preview JSON**: See real-time output in the right panel
4. **Save Profile**: Data is automatically saved locally
5. **Export Data**: Copy JSON for use with Python backend

### Using the Python Backend

1. **Start Application**: Run `python app.py`
2. **Open Interface**: Go to `http://localhost:7860`
3. **Upload Images**: Add your photos
4. **Configure Settings**: Adjust AI parameters
5. **Generate Portrait**: Process and download results

---

## 🔄 Development Workflow

### For Contributors

#### Setting Up Development Environment
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/FluxPortrait.git
cd FluxPortrait

# Add upstream remote
git remote add upstream https://github.com/kmamine/FluxPortrait.git

# Create development branch
git checkout -b feature/your-feature-name

# Setup both environments
# Python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# React
cd web-app
npm install
npm run dev
```

#### Available Scripts

**Python Development:**
```bash
# Run main application
python app.py

# Run simple form
python user_form_simple.py

# Run tests
python -m pytest tests/

# Format code
black apex/
```

**React Development:**
```bash
# Development server with hot reload
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint

# Type checking
npx tsc --noEmit
```

### Project Structure
```
FluxPortrait/
├── 🐍 Python Backend
│   ├── apex/                    # Core Python package
│   │   ├── config/             # Configuration settings
│   │   ├── core/               # Core functionality
│   │   ├── models/             # Data models
│   │   ├── ui/                 # Gradio interface
│   │   └── utils/              # Utility functions
│   ├── data/                   # Data storage
│   ├── tests/                  # Python tests
│   ├── app.py                  # Main application
│   ├── requirements.txt        # Python dependencies
│   └── setup.py               # Package setup
├── ⚛️ React Frontend
│   ├── web-app/
│   │   ├── src/               # Source code
│   │   │   ├── components/    # React components
│   │   │   ├── constants/     # Configuration
│   │   │   ├── types/         # TypeScript types
│   │   │   └── utils/         # Utility functions
│   │   ├── public/            # Static assets
│   │   ├── package.json       # Node.js dependencies
│   │   ├── setup.sh          # Setup script
│   │   └── check-requirements.sh
└── 📚 Documentation
    ├── README.md              # Main repository README
    ├── README-WebApp.md       # Web app specific README
    └── SETUP-GUIDE.md         # This comprehensive guide
```

---

## 🚀 Production Deployment

### React Web App Deployment

#### Vercel (Recommended)
```bash
# Install Vercel CLI
npm install -g vercel

# Build and deploy
cd web-app
npm run build
vercel --prod
```

#### Netlify
```bash
# Build the app
npm run build

# Deploy dist/ folder to Netlify
# Or connect GitHub repository for auto-deployment
```

#### Docker Deployment
```dockerfile
# Dockerfile for React app
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "preview"]
```

### Python Backend Deployment

#### Docker
```dockerfile
# Dockerfile for Python backend
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 7860
CMD ["python", "app.py"]
```

#### Heroku
```bash
# Create Procfile
echo "web: python app.py" > Procfile

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

---

## 🤝 Contributing

### How to Contribute

1. **Fork the Repository**
   ```bash
   # Click "Fork" on GitHub, then:
   git clone https://github.com/YOUR_USERNAME/FluxPortrait.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Changes**
   - Follow existing code style
   - Add tests for new features
   - Update documentation

4. **Test Your Changes**
   ```bash
   # Test Python code
   python -m pytest tests/
   
   # Test React code
   cd web-app
   npm run lint
   npm run build
   ```

5. **Submit Pull Request**
   ```bash
   git add .
   git commit -m "Add amazing feature"
   git push origin feature/amazing-feature
   # Create PR on GitHub
   ```

### Development Guidelines

- **Code Style**: Follow existing patterns
- **TypeScript**: Use proper types in React components
- **Python**: Follow PEP 8 guidelines
- **Documentation**: Update README files for changes
- **Tests**: Add tests for new functionality

---

## 📞 Support

### Getting Help

1. **Check This Guide**: Most issues are covered here
2. **Run Diagnostics**: Use `./check-requirements.sh`
3. **GitHub Issues**: Create an issue with details
4. **Documentation**: Check other README files

### Reporting Issues

Include this information when reporting bugs:

```bash
# System information
uname -a                    # Operating system
node --version             # Node.js version
python --version           # Python version
npm --version              # npm version

# Error logs
cat ~/.npm/_logs/*.log     # npm errors
# Include full error output
```

### Common Questions

**Q: Can I use the web app without the Python backend?**
A: Yes! The web app generates JSON profiles that can be used independently.

**Q: Which setup should I use?**
A: For most users, the React web app is recommended. Use Python backend only if you need AI processing.

**Q: Can I deploy this to my own server?**
A: Yes! See the production deployment section for instructions.

**Q: Is this project free to use?**
A: Yes, this is an open-source project. Check the license for details.

---

## 🏆 Success Checklist

After following this guide, you should have:

- [ ] ✅ Node.js 18+ installed and working
- [ ] ✅ Python 3.8+ installed (if using backend)
- [ ] ✅ Repository cloned successfully
- [ ] ✅ React web app running at `http://localhost:3000`
- [ ] ✅ Python backend running at `http://localhost:7860` (if used)
- [ ] ✅ All dependencies installed without errors
- [ ] ✅ Able to create and save profiles
- [ ] ✅ Mobile-responsive interface working
- [ ] ✅ JSON export functionality working

**Congratulations! 🎉 You have successfully set up the APEX Portrait Generator!**

---

*Made with ❤️ for creating amazing AI portraits*

**Last Updated**: July 21, 2025  
**Version**: 1.0.0  
**Compatibility**: Node.js 18+, Python 3.8+, All modern browsers
