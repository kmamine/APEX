#!/bin/bash

# APEX Web App Setup Script
echo "🖼️ APEX Portrait Generator - Web App Setup"
echo "============================================"
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed."
    echo ""
    echo "Please install Node.js first:"
    echo ""
    echo "Option 1 - Using Homebrew (macOS):"
    echo "  /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    echo "  echo 'eval \"\$(/opt/homebrew/bin/brew shellenv)\"' >> ~/.zprofile"
    echo "  eval \"\$(/opt/homebrew/bin/brew shellenv)\""
    echo "  brew install node"
    echo ""
    echo "Option 2 - Using NVM (Cross-platform):"
    echo "  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash"
    echo "  source ~/.zshrc"
    echo "  nvm install --lts"
    echo "  nvm use --lts"
    echo ""
    echo "Option 3 - Download from https://nodejs.org/"
    echo ""
    echo "Then run this script again."
    exit 1
fi

echo "✅ Node.js found: $(node --version)"

# Check if npm is available
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not available."
    echo "Please reinstall Node.js which includes npm."
    exit 1
fi

echo "✅ npm found: $(npm --version)"

# Navigate to the script directory
cd "$(dirname "$0")"

echo ""
echo "� Current directory: $(pwd)"
echo ""

# Check if package.json exists
if [ ! -f "package.json" ]; then
    echo "❌ package.json not found. Make sure you're in the web-app directory."
    exit 1
fi

echo "�📦 Installing dependencies..."
echo "This may take a few minutes..."
echo ""

npm install

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Dependencies installed successfully!"
    echo ""
    echo "🚀 Starting development server..."
    echo "The app will be available at:"
    echo "  Local:   http://localhost:3000"
    echo "  Network: Available on your local network"
    echo ""
    echo "📱 Mobile Testing:"
    echo "  Use the Network URL on your phone/tablet"
    echo ""
    echo "⌨️  Keyboard Shortcuts:"
    echo "  Press 'h + Enter' to show Vite help"
    echo "  Press 'Ctrl+C' to stop the server"
    echo ""
    echo "🎯 Ready to use APEX Portrait Generator!"
    echo "============================================"
    echo ""
    
    # Start the development server
    npm run dev
else
    echo ""
    echo "❌ Failed to install dependencies."
    echo ""
    echo "🔧 Troubleshooting:"
    echo "1. Make sure you have a stable internet connection"
    echo "2. Try clearing npm cache: npm cache clean --force"
    echo "3. Delete node_modules and try again:"
    echo "   rm -rf node_modules package-lock.json"
    echo "   npm install"
    echo "4. Check if you have the latest Node.js version"
    echo ""
    exit 1
fi
