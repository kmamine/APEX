# APEX Portrait Generator - Responsive Web App

A modern, responsive React web application that replicates the functionality of your APEX Portrait Generator Gradio interface. Built with React, TypeScript, and Tailwind CSS for optimal mobile and desktop experience.

## 🚀 Features

- **📱 Responsive Design**: Works seamlessly on mobile, tablet, and desktop
- **🎯 Preset Management**: Quick-start templates for common portrait scenarios
- **📝 Comprehensive Form**: Collect all portrait preferences and settings
- **💾 Profile Management**: Save and load profiles using browser localStorage
- **🎨 Real-time Prompt Generation**: Generate AI prompts based on user preferences
- **📄 JSON Export**: Export profiles for use with your Python backend
- **♿ Accessibility**: Screen reader friendly with proper ARIA labels
- **⚡ Fast Performance**: Optimized with Vite and modern React patterns

## 🛠️ Technology Stack

- **React 18** with TypeScript
- **Vite** for fast development and building
- **Tailwind CSS** for responsive styling
- **Modern CSS Grid & Flexbox** for layouts
- **Browser localStorage** for profile persistence

## 📦 Prerequisites

Before running this application, make sure you have:

- **Node.js** (version 16 or higher)
- **npm** package manager

### Installing Node.js on macOS

If you don't have Node.js installed, here are the installation options:

#### Option 1: Using Homebrew (Recommended)
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add Homebrew to your PATH (if not already done)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/$(whoami)/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# Install Node.js
brew install node
```

#### Option 2: Using Node Version Manager (NVM)
```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Restart terminal or source your profile
source ~/.zshrc

# Install latest LTS Node.js
nvm install --lts
nvm use --lts
```

## 🏃‍♂️ Quick Start

### Step 1: Navigate to the web app directory
```bash
cd /Users/marouane/Desktop/FluxPortrait/web-app
```

### Step 2: Install dependencies
```bash
npm install
```

### Step 3: Start the development server
```bash
npm run dev
```

### Step 4: Open your browser
The app will be available at:
- **Local**: http://localhost:3000
- **Network**: Available on your local network for mobile testing

## 📝 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript type checking

## 📱 Responsive Features

### Mobile-First Design
- **Collapsible sections** for better mobile navigation (tap section headers)
- **Touch-friendly** buttons and form controls
- **Single-column layout** optimized for mobile screens
- **Optimized typography** for mobile reading

### Desktop Enhancements
- **Two-column layout** for efficient screen space usage
- **All sections expanded** by default for easy overview
- **Larger click targets** for precision
- **Keyboard navigation** support

## 🎯 Application Features

### Form Sections
1. **🎯 Quick Start Presets**
   - LinkedIn Professional
   - Creative Portfolio
   - Academic Profile
   - Startup Founder
   - Executive Portrait

2. **🔧 Basic Settings**
   - Purpose (LinkedIn, Resume, Corporate Website, etc.)
   - Attire (Business Formal, Business Casual, etc.)
   - Background (Corporate Office, Plain Color, etc.)
   - Vibe (Confident, Friendly, Approachable, etc.)

3. **⚙️ Advanced Settings**
   - Lighting Style (Natural Light, Studio Lighting, etc.)
   - Overall Mood (Professional, Casual, etc.)
   - Demographics (Age Range, Gender, Ethnicity)
   - Resolution (Standard, Wide, Portrait, High-Res)

4. **📝 Additional Information**
   - Custom notes and specific requirements
   - Profile saving options

### Output Display
- **📄 Complete Style Profile**: JSON format identical to Python backend
- **🎨 Generated Flux Prompt**: AI-optimized prompt for image generation
- **💾 Profile Management**: Save/load from browser storage
- **📊 Status Messages**: Real-time feedback and validation

## 🔧 Integration with Your Python Backend

The web app generates the same JSON structure as your Python application:

```json
{
  "basic_info": {
    "purpose": "LinkedIn",
    "attire": "Business Formal",
    "background": "Corporate Office",
    "vibe": "Confident"
  },
  "advanced_settings": {
    "lighting": "Professional Flash",
    "mood": "Professional",
    "age_range": "30-40",
    "gender": "Not Specified",
    "ethnicity": "Not Specified",
    "resolution": "1024x1024 (Standard)"
  },
  "additional_info": {
    "reference_photo": null,
    "custom_notes": "Professional headshot...",
    "preset_used": "LinkedIn Professional"
  },
  "metadata": {
    "timestamp": "2025-07-20 23:30:00",
    "version": "2.0",
    "created_by": "APEX Portrait Generator (Web)"
  },
  "generated_prompt": "Professional portrait for linkedin..."
}
```

### Integration Options

1. **Standalone Use** (Current setup)
   - Use the web form to generate profiles
   - Copy JSON output to use with your Python backend
   - Save profiles locally for later use

2. **API Integration** (Future enhancement)
   - Add endpoints to your Python Flask/FastAPI server
   - Modify form submission to send data directly to backend
   - Real-time integration with portrait generation pipeline

## 🎨 Customization

### Styling
- **Colors**: Edit `tailwind.config.js` for custom brand colors
- **Fonts**: Modify the Google Fonts import in `src/index.css`
- **Layout**: Adjust component styles in individual `.tsx` files

### Form Options
- **Dropdown Options**: Edit `src/constants/options.ts`
- **Presets**: Add/modify presets in the `presets` object
- **Validation**: Customize rules in `src/utils/profileManager.ts`

### Adding New Features
- **New Form Fields**: Update types in `src/types/index.ts`
- **New Components**: Add to `src/components/`
- **New Utilities**: Add to `src/utils/`

## 🚀 Deployment

### Build for Production
```bash
npm run build
```

### Deploy Options
- **Netlify**: Drag and drop the `dist` folder
- **Vercel**: Connect your Git repository
- **GitHub Pages**: Use the built files
- **Your own server**: Serve the `dist` folder with any web server

### Environment Setup for Production
Create a `.env.production` file if needed:
```env
VITE_API_URL=https://your-api-domain.com
VITE_APP_TITLE=APEX Portrait Generator
```

## 🔧 Troubleshooting

### Common Issues and Solutions

1. **Node.js not found**
   ```bash
   # Check if Node.js is installed
   node --version
   npm --version
   
   # If not installed, follow the prerequisites section
   ```

2. **Port already in use**
   ```bash
   # Kill process on port 3000
   lsof -ti:3000 | xargs kill -9
   
   # Or change port in vite.config.ts
   ```

3. **CSS compilation errors**
   - Ensure all `@import` statements are at the top of CSS files
   - Check for proper Tailwind class names
   - Run `npm run build` to check for build errors

4. **TypeScript errors**
   ```bash
   # Check for type errors
   npm run type-check
   
   # Fix common issues in src/types/index.ts
   ```

5. **Dependencies issues**
   ```bash
   # Clear node_modules and reinstall
   rm -rf node_modules package-lock.json
   npm install
   ```

### Development Tips
- Use browser developer tools for responsive testing
- Check the browser console for JavaScript errors
- Use React Developer Tools extension for debugging
- Test on actual mobile devices using the network URL

## 📞 Support & Maintenance

### Logging and Debugging
- Browser console shows React errors and warnings
- Network tab shows API calls (when integrated)
- React DevTools for component state inspection

### Performance Monitoring
- Lighthouse scores for performance optimization
- Bundle analyzer: `npm run build && npx vite-bundle-analyzer dist`

### Security Considerations
- All data stored locally in browser
- No sensitive information transmitted
- HTTPS recommended for production deployment

## 🎯 Benefits Over Gradio Interface

1. **📱 Mobile-First**: Perfect responsive design for all devices
2. **⚡ Faster**: No Python server needed for the form interface
3. **🎨 Modern UI**: Clean, professional design with better UX
4. **🔧 Customizable**: Easy to modify colors, layout, and options
5. **🌐 Deployable**: Can host anywhere with static hosting
6. **♿ Accessible**: Better screen reader support and ARIA labels
7. **📱 Progressive**: Works offline after first load
8. **💾 Persistent**: Saves user preferences and profiles locally

## 🔄 Workflow Integration

### With Your Python Backend
1. **Development**: Use web form to generate and test profiles
2. **Production**: Copy JSON profiles to your Python scripts
3. **Automation**: Potential for API integration in future

### With AI Generation Pipeline
1. Use generated prompts directly with Flux models
2. Import/export profiles for batch processing
3. Version control for prompt templates

## 📈 Future Enhancements

- **Real-time API integration** with your Python backend
- **Image upload and preview** functionality
- **Profile templates marketplace**
- **Advanced prompt customization**
- **Multi-language support**
- **Dark mode theme**
- **Export to multiple formats** (CSV, PDF, etc.)

## 📄 License

This project is part of the APEX Portrait Generator system. See the main project for licensing information.

---

**🎉 Your responsive APEX Portrait Generator web application is ready for production use!**

For questions or issues, check the troubleshooting section above or refer to the browser console for detailed error messages.
