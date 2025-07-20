#!/bin/bash

# APEX Web App Setup Script
echo "🖼️ APEX Portrait Generator - Web App Setup"
echo "============================================"

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed."
    echo ""
    echo "Please install Node.js first:"
    echo "Option 1 - Using Homebrew:"
    echo "  brew install node"
    echo ""
    echo "Option 2 - Using NVM (recommended):"
    echo "  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash"
    echo "  source ~/.zshrc"
    echo "  nvm install --lts"
    echo "  nvm use --lts"
    echo ""
    echo "Then run this script again."
    exit 1
fi

echo "✅ Node.js found: $(node --version)"

# Check if npm is available
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not available."
    exit 1
fi

echo "✅ npm found: $(npm --version)"

# Navigate to the web app directory
cd "$(dirname "$0")"

echo ""
echo "📦 Installing dependencies..."
npm install

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
    echo ""
    echo "🚀 Starting development server..."
    echo "The app will open at http://localhost:3000"
    echo ""
    echo "Press Ctrl+C to stop the server"
    echo ""
    npm run dev
else
    echo "❌ Failed to install dependencies."
    echo "Please check the error messages above."
    exit 1
fi
