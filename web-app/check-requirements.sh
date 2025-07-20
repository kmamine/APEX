#!/bin/bash

# APEX Web App - System Requirements Checker
echo "🔍 APEX Web App - System Requirements Check"
echo "==========================================="
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to check command existence
check_command() {
    if command -v "$1" &> /dev/null; then
        echo -e "${GREEN}✅ $1${NC}: $(command -v "$1")"
        return 0
    else
        echo -e "${RED}❌ $1${NC}: Not found"
        return 1
    fi
}

# Function to check version
check_version() {
    local cmd="$1"
    local min_version="$2"
    local current_version="$3"
    
    echo -e "${BLUE}📦 $cmd version${NC}: $current_version"
    
    # Simple version comparison (works for most cases)
    if [[ "$current_version" == "$min_version"* ]] || [[ "$current_version" > "$min_version" ]]; then
        echo -e "${GREEN}✅ Version OK${NC} (>= $min_version)"
        return 0
    else
        echo -e "${YELLOW}⚠️  Version Warning${NC} (recommended >= $min_version)"
        return 1
    fi
}

echo "🖥️  Operating System: $(uname -s)"
echo "🏗️  Architecture: $(uname -m)"
echo ""

# Check Node.js
echo "🔍 Checking Node.js..."
if check_command "node"; then
    NODE_VERSION=$(node --version | sed 's/v//')
    check_version "Node.js" "18.0.0" "$NODE_VERSION"
else
    echo -e "${YELLOW}📋 Install Node.js:${NC}"
    echo "  • Homebrew (macOS): brew install node"
    echo "  • NVM: curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash"
    echo "  • Official: https://nodejs.org/"
fi

echo ""

# Check npm
echo "🔍 Checking npm..."
if check_command "npm"; then
    NPM_VERSION=$(npm --version)
    check_version "npm" "8.0.0" "$NPM_VERSION"
fi

echo ""

# Check git
echo "🔍 Checking git..."
if check_command "git"; then
    GIT_VERSION=$(git --version | sed 's/git version //')
    check_version "git" "2.0.0" "$GIT_VERSION"
else
    echo -e "${YELLOW}📋 Install git:${NC}"
    echo "  • Homebrew (macOS): brew install git"
    echo "  • Official: https://git-scm.com/"
fi

echo ""

# Check if we're in the right directory
echo "🔍 Checking project structure..."
if [ -f "package.json" ]; then
    echo -e "${GREEN}✅ package.json${NC}: Found"
    
    # Check if node_modules exists
    if [ -d "node_modules" ]; then
        echo -e "${GREEN}✅ node_modules${NC}: Dependencies installed"
    else
        echo -e "${YELLOW}⚠️  node_modules${NC}: Not found (run 'npm install')"
    fi
    
    # Check if src directory exists
    if [ -d "src" ]; then
        echo -e "${GREEN}✅ src/${NC}: Source code found"
    else
        echo -e "${RED}❌ src/${NC}: Source directory missing"
    fi
else
    echo -e "${RED}❌ package.json${NC}: Not found"
    echo -e "${YELLOW}💡 Make sure you're in the web-app directory${NC}"
fi

echo ""

# Network check
echo "🔍 Checking network connectivity..."
if ping -c 1 google.com &> /dev/null; then
    echo -e "${GREEN}✅ Internet connection${NC}: Available"
else
    echo -e "${YELLOW}⚠️  Internet connection${NC}: May be limited"
    echo "   This could affect npm package installation"
fi

echo ""

# Disk space check
echo "🔍 Checking available disk space..."
AVAILABLE_SPACE=$(df -h . | tail -1 | awk '{print $4}')
echo -e "${BLUE}💾 Available space${NC}: $AVAILABLE_SPACE"

echo ""
echo "🎯 Summary:"
echo "=========="

if command -v node &> /dev/null && command -v npm &> /dev/null; then
    echo -e "${GREEN}✅ Ready to run APEX Web App!${NC}"
    echo ""
    echo "🚀 Next steps:"
    echo "  1. cd FluxPortrait/web-app"
    echo "  2. ./setup.sh (or npm install && npm run dev)"
    echo "  3. Open http://localhost:3000"
else
    echo -e "${YELLOW}⚠️  Please install missing requirements first${NC}"
    echo ""
    echo "📋 Installation guide:"
    echo "  See README-WebApp.md for detailed instructions"
fi

echo ""
