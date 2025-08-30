# Deployment Guide for Render

This project contains both a Next.js frontend and a FastAPI backend. Here are the deployment options:

## Option 1: Deploy Backend Only (Recommended for API-first deployment)

### Files Created for Backend Deployment:
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification  
- `Procfile` - Process file for Render
- `.env.example` - Environment variables template

### Render Service Configuration:
1. **Service Type**: Web Service
2. **Environment**: Python
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `python backend/main.py`
5. **Environment Variables**:
   - `GEMINI_API_KEY`: Your Google Gemini AI API key
   - `PORT`: (Auto-set by Render)

### Manual Steps on Render:
1. Connect your GitHub repository
2. Set environment variables in Render dashboard
3. Deploy the service

## Option 2: Deploy as Separate Services

### Backend Service:
- Repository: Same repo
- Build Command: `pip install -r requirements.txt`
- Start Command: `python backend/main.py`
- Environment Variables: `GEMINI_API_KEY`

### Frontend Service:
- Repository: Same repo  
- Build Command: `npm install && npm run build`
- Start Command: `npm start`
- Environment Variables: Update API endpoint to backend service URL

## Environment Variables Required:
- `GEMINI_API_KEY`: Get from Google AI Studio (https://ai.google.dev/)

## API Endpoints Available:
- `GET /`: Health check
- `POST /analyze-coordinates`: Coordinate-based flood risk analysis
- `POST /analyze-image`: Image-based flood risk analysis
- `GET /docs`: API documentation (Swagger UI)

## Important Notes:
- Make sure to set the `GEMINI_API_KEY` in Render's environment variables
- The backend is configured to use the PORT environment variable automatically
- CORS is configured to allow frontend connections
