# 🌊 Flood Detection System

A modern, AI-powered flood risk assessment system built with Next.js and FastAPI. Analyze flood risks using coordinates or image uploads with Gemini AI integration.

![Flood Detection System](https://img.shields.io/badge/status-active-brightgreen) ![Next.js](https://img.shields.io/badge/Next.js-15.5.2-black) ![FastAPI](https://img.shields.io/badge/FastAPI-latest-green) ![Python](https://img.shields.io/badge/Python-3.13-blue)

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

### Required API Keys

1. **Gemini AI API Key** (Required)
   - Get from: https://makersuite.google.com/app/apikey
   - Add to `backend/.env`: `GEMINI_API_KEY=your_key_here`

2. **Google Maps API Key** (Optional - for map features)
   - Get from: https://console.cloud.google.com/
   - Add to `.env.local`: `NEXT_PUBLIC_GOOGLE_MAPS_API_KEY=your_key_here`

## 📁 Project Structure

```
flood-detection-system/
├── app/                    # Next.js app directory
│   ├── globals.css        # Global styles
│   ├── layout.tsx         # Root layout
│   └── page.tsx           # Main application page
├── backend/               # FastAPI backend
│   ├── main.py           # FastAPI application
│   ├── start.py          # Server startup script
│   ├── requirements.txt  # Python dependencies
│   └── .env.example      # Environment variables template
├── components/           # React components
│   └── ui/              # UI components (shadcn/ui)
├── lib/                 # Utility functions
├── public/              # Static assets
├── .env.local.example   # Frontend environment template
├── package.json         # Node.js dependencies
└── README.md           # This file
```

## 🔄 API Endpoints

### Coordinate Analysis
```http
POST /api/analyze/coordinates
Content-Type: application/json

{
  "latitude": 40.7128,
  "longitude": -74.0060
}
```

### Image Analysis
```http
POST /api/analyze/image
Content-Type: multipart/form-data

file: [image file]
```

## 🛠️ Development

### Frontend
- **Framework**: Next.js 15.5.2 with TypeScript
- **Styling**: Tailwind CSS + shadcn/ui
- **State Management**: React hooks

### Backend
- **Framework**: FastAPI with Python 3.13
- **AI Integration**: Google Gemini AI
- **File Handling**: Python-multipart for image uploads

## 📦 Dependencies

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

## 🆘 Support

If you encounter any issues:

1. Check the [API Documentation](http://localhost:8000/docs) when the backend is running
2. Ensure all environment variables are properly set
3. Verify your API keys are valid
4. Check the console for error messages

## 🔮 Future Enhancements

- [ ] Interactive map integration
- [ ] Historical flood data analysis
- [ ] Multiple AI model support
- [ ] Weather API integration
- [ ] Real-time alerts system
- [ ] Mobile app version

---

Made with ❤️ for flood risk assessment and community safety.
