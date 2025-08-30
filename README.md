# 🌊 Flood Detection System

<div align="center">

A modern, AI-powered flood risk assessment system built with Next.js and FastAPI. Analyze flood risks using coordinates or image uploads with Gemini AI integration.

![Screenshot](https://i.postimg.cc/mZFWtBXQ/Flood-Detection-System-Google-Chrome-30-08-2025-1-30-44-pm.png)

![Flood Detection System](https://img.shields.io/badge/status-active-brightgreen) ![Next.js](https://img.shields.io/badge/Next.js-15.5.2-black) ![FastAPI](https://img.shields.io/badge/FastAPI-latest-green) ![Python](https://img.shields.io/badge/Python-3.13-blue)

</div>

## ✨ Features

- 📍 **Coordinate-based Analysis**: Enter latitude/longitude for location-specific flood risk assessment
- 🖼️ **Image Analysis**: Upload terrain images for AI-powered flood risk evaluation  
- 🤖 **AI-Powered**: Uses Google's Gemini AI for intelligent risk assessment
- 📱 **Responsive Design**: Modern, mobile-friendly interface
- 🎯 **Real-time Analysis**: Get instant flood risk reports with recommendations
- 🌍 **Location Detection**: Automatically identifies places from coordinates

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ 
- Python 3.13+
- Google Gemini AI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flood-detection-system.git
   cd flood-detection-system
   ```

2. **Install frontend dependencies**
   ```bash
   npm install
   ```

3. **Install backend dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   
   **Frontend (.env.local)**:
   ```bash
   cp .env.local.example .env.local
   # Edit .env.local and add your Google Maps API key (optional)
   ```
   
   **Backend (backend/.env)**:
   ```bash
   cd backend
   cp .env.example .env
   # Edit .env and add your Gemini AI API key (required)
   ```

5. **Start the servers**
   
   **Backend** (in backend/ directory):
   ```bash
   python start.py
   ```
   
   **Frontend** (in root directory):
   ```bash
   npm run dev
   ```

6. **Open your browser**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 🔧 Configuration

### Required API Key

 **Gemini AI API Key** (Required)
   - Get from: https://makersuite.google.com/app/apikey
   - Add to `backend/.env`: `GEMINI_API_KEY=your_key_here`


## 🛠️ Development 

### Frontend
- Next.js 15.5.2
- React 19
- TypeScript
- Tailwind CSS
- shadcn/ui components
- Lucide React icons

### Backend
- FastAPI
- Uvicorn
- Google Generative AI
- Python-multipart
- Pillow (PIL)
- Python-dotenv

## 🔒 Security

- API keys are stored in environment variables
- File upload validation and size limits
- CORS configuration for secure cross-origin requests
- Input validation for coordinates and file types

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

Made with ❤️ for community safety.
