# 🖼️ APEX Portrait Generator - Web App

A responsive React web application for the APEX Portrait Generator, providing an intuitive interface for creating AI-generated professional portraits.

## 🌟 Features

- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **🎨 Modern UI**: Clean, professional interface built with React and Tailwind CSS
- **⚡ Fast & Lightweight**: Built with Vite for optimal performance
- **🔄 Real-time Preview**: See JSON output as you fill the form
- **📊 Preset Profiles**: Quick-start templates for different use cases
- **💾 Local Storage**: Automatically saves your work locally
- **🖥️ Cross-platform**: Works on macOS, Windows, and Linux

## 🚀 Quick Start

### Prerequisites

- **Node.js 18+** (Required)
- **npm** (Comes with Node.js)

### Installation Options

#### Option 1: Automated Setup (Recommended)
```bash
git clone https://github.com/kmamine/FluxPortrait.git
cd FluxPortrait/web-app
chmod +x setup.sh
./setup.sh
```

#### Option 2: Manual Setup
```bash
git clone https://github.com/kmamine/FluxPortrait.git
cd FluxPortrait/web-app
npm install
npm run dev
```

### Installing Node.js (if not installed)

#### macOS (Homebrew)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
brew install node
```

#### Cross-platform (NVM - Recommended)
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.zshrc  # or source ~/.bashrc on Linux
nvm install --lts
nvm use --lts
```

#### Windows
Download from [nodejs.org](https://nodejs.org/) or use Chocolatey:
```bash
choco install nodejs
```

## 🖥️ Usage

1. **Start the app**: Run `npm run dev` or use the setup script
2. **Access locally**: Open http://localhost:3000
3. **Mobile testing**: Use the network URL shown in terminal
4. **Create profiles**: Use presets or fill forms manually
5. **Export data**: Copy the generated JSON for use with the Python backend

## 📁 Project Structure

```
web-app/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Select.tsx
│   │   ├── Textarea.tsx
│   │   ├── Card.tsx
│   │   ├── FormSection.tsx
│   │   └── PortraitForm.tsx
│   ├── constants/           # Configuration and options
│   │   └── options.ts
│   ├── types/              # TypeScript definitions
│   │   └── profile.ts
│   ├── utils/              # Utility functions
│   │   ├── profileManager.ts
│   │   └── validation.ts
│   ├── App.tsx             # Main application component
│   ├── main.tsx           # Application entry point
│   └── index.css          # Global styles
├── public/                 # Static assets
├── package.json           # Dependencies and scripts
├── setup.sh              # Automated setup script
└── README.md             # This file
```

## 🎨 Available Presets

- **👔 LinkedIn Professional**: Corporate headshots and business profiles
- **🎨 Creative Portfolio**: Artistic and creative professional portraits
- **🎓 Academic Profile**: University and research institution portraits
- **🚀 Startup Founder**: Modern entrepreneur and tech leader looks
- **💼 Executive Portrait**: C-suite and senior leadership portraits

## 💡 Available Scripts

```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run preview      # Preview production build
npm run lint         # Run ESLint
```

## 🛠️ Development

### Tech Stack
- **React 18**: Modern React with hooks and functional components
- **TypeScript**: Type-safe JavaScript development
- **Vite**: Fast build tool and development server
- **Tailwind CSS**: Utility-first CSS framework
- **ESLint**: Code linting and formatting

### Development Server
The development server runs on `http://localhost:3000` with hot module replacement for instant updates.

### Building for Production
```bash
npm run build
```
This creates an optimized build in the `dist/` directory.

## 📱 Mobile Support

The app is fully responsive and tested on:
- **📱 iOS Safari**: iPhone and iPad
- **🤖 Android Chrome**: Phones and tablets
- **🖥️ Desktop**: Chrome, Firefox, Safari, Edge

## 🔧 Troubleshooting

### Common Issues

**"Node.js not found"**
```bash
# Install Node.js using one of the methods above
node --version  # Should show v18+ or higher
```

**"npm install fails"**
```bash
# Clear cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**"Port 3000 already in use"**
```bash
# Kill process using port 3000
lsof -ti:3000 | xargs kill -9
# Or use a different port
npm run dev -- --port 3001
```

**"Module not found"**
```bash
# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Submit a pull request

## 📄 License

This project is part of the APEX Portrait Generator suite. See the main repository for license information.

## 🔗 Related

- **Python Backend**: See the main repository for the Python-based APEX system
- **Original Gradio Interface**: Available in the main repository
- **Documentation**: Full documentation in the main repository

---

Made with ❤️ for creating amazing AI portraits
