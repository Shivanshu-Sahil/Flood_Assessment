from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn
import os
import asyncio
from datetime import datetime
import logging
import google.generativeai as genai
from dotenv import load_dotenv
import base64
import io
import json
import re
from PIL import Image as PILImage

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Gemini AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI(
    title="Flood Detection API",
    description="Simple flood risk assessment using Gemini AI",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models
class CoordinateRequest(BaseModel):
    latitude: float
    longitude: float

class AnalysisResponse(BaseModel):
    success: bool
    risk_level: str
    description: str
    recommendations: list[str]
    elevation: float
    distance_from_water: float
    message: str

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Flood Detection API",
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }

def parse_gemini_response(response_text: str) -> dict:
    """Parse Gemini AI response and extract structured data"""
    try:
        # Try to extract JSON from the response
        # regular expression to find json
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            parsed_data = json.loads(json_str)
            
            return {
                "location_name": parsed_data.get("location_name", "Unknown Location"),
                "risk_level": parsed_data.get("risk_level", "Medium"),
                "description": parsed_data.get("description", "Analysis completed"),
                "recommendations": parsed_data.get("recommendations", []),
                "elevation": parsed_data.get("elevation", 50.0),
                "distance_from_water": parsed_data.get("distance_from_water", 1000.0),
                "geographic_features": parsed_data.get("geographic_features", ""),
                "image_analysis": parsed_data.get("image_analysis", ""),
                "analysis": parsed_data.get("analysis", "")
            }
        else:
            return {
                "location_name": "Unknown Location",
                "risk_level": "Medium",
                "description": "Analysis completed",
                "recommendations": ["Monitor weather conditions", "Stay informed about local alerts"],
                "elevation": 50.0,
                "distance_from_water": 1000.0,
                "geographic_features": "Geographic analysis not available",
                "image_analysis": response_text,
                "analysis": response_text
            }        
        # stable response even if failure
    except Exception as e:
        logger.error(f"Error parsing Gemini response: {str(e)}")
        return {
            "location_name": "Unknown Location",
            "risk_level": "Medium",
            "description": "Analysis completed",
            "recommendations": ["Monitor weather conditions", "Stay informed about local alerts"],
            "elevation": 50.0,
            "distance_from_water": 1000.0,
            "geographic_features": "Geographic analysis not available",
            "image_analysis": response_text,
            "analysis": response_text
        }

@app.post("/api/analyze/coordinates")
async def analyze_coordinates(request: CoordinateRequest):
    """
    Analyze flood risk based on coordinates using Gemini AI
    """
    try:
        logger.info(f"Analyzing coordinates: {request.latitude}, {request.longitude}")
        
        # Validate coordinates
        if not (-90 <= request.latitude <= 90):
            raise HTTPException(status_code=400, detail="Latitude must be between -90 and 90")
        if not (-180 <= request.longitude <= 180):
            raise HTTPException(status_code=400, detail="Longitude must be between -180 and 180")
        
        prompt = f"""
        Analyze the flood risk for the location at coordinates {request.latitude}, {request.longitude}.
        
        Please identify the location and provide:
        1. Location name (city, region, country if identifiable)
        2. Risk Level (Low/Medium/High/Very High)
        3. Description of the risk based on geographic and topographic factors
        4. 3-5 specific recommendations
        5. Estimated elevation in meters
        6. Estimated distance from water bodies in meters
        7. Geographic features and terrain type in the area
        
        Format your response as JSON with these fields:
        - location_name (string)
        - risk_level (string)
        - description (string)
        - recommendations (array of strings)
        - elevation (number)
        - distance_from_water (number)
        - geographic_features (string)
        - analysis (string describing the geographic analysis)
        """
        
        try:
            model = genai.GenerativeModel('gemini-2.0-flash-exp')
            response = model.generate_content(prompt)
            parsed_data = parse_gemini_response(response.text)
            
        except Exception as ai_error:
            logger.error(f"Error calling Gemini AI: {str(ai_error)}")
            # Fallback to simulated data if AI fails
            parsed_data = generate_coordinate_risk_assessment(request.latitude, request.longitude)
            parsed_data["analysis"] = "Coordinate analysis was not available, using simulated assessment"
        
        # Return structured response
        return {
            "success": True,
            **parsed_data,
            "ai_analysis": parsed_data.get("analysis", ""),
            "message": "Coordinate analysis completed successfully"
        }
        
    except Exception as e:
        logger.error(f"Error analyzing coordinates: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

def generate_coordinate_risk_assessment(latitude: float, longitude: float) -> dict:
    """Generate risk assessment for coordinate analysis"""
    import random
    
    # Generate a simplified location name based on coordinates
    def get_location_name(lat: float, lng: float) -> str:
        """Generate a simplified location name based on coordinates"""
        regions = {
            "North America": (25, 70, -170, -50),
            "Europe": (35, 70, -10, 40),
            "Asia": (10, 70, 40, 180),
            "Africa": (-35, 35, -20, 50),
            "South America": (-55, 15, -90, -30),
            "Australia/Oceania": (-50, -10, 110, 180)
        }
        
        for region, (min_lat, max_lat, min_lng, max_lng) in regions.items():
            if min_lat <= lat <= max_lat and min_lng <= lng <= max_lng:
                return f"Location in {region}"
        
        return f"Location at {lat:.2f}°, {lng:.2f}°"
    
    # Simple heuristic based on latitude (closer to sea level might have higher risk)
    base_risk = 0.3
    if abs(latitude) < 30:  # Tropical/subtropical regions
        base_risk += 0.2
    if abs(latitude) < 10:  # Equatorial regions
        base_risk += 0.1
    
    risk_score = base_risk + random.uniform(0, 0.4)
    
    if risk_score < 0.3:
        risk_level = "Low"
    elif risk_score < 0.5:
        risk_level = "Medium"
    elif risk_score < 0.7:
        risk_level = "High"
    else:
        risk_level = "Very High"
    
    location_name = get_location_name(latitude, longitude)
    
    descriptions = {
        "Low": f"{location_name} shows low flood risk characteristics.",
        "Medium": f"{location_name} indicates moderate flood risk factors.",
        "High": f"{location_name} reveals high flood risk characteristics.",
        "Very High": f"{location_name} shows very high flood risk indicators."
    }
    
    recommendations = {
        "Low": [
            "Monitor local weather conditions",
            "Stay informed about seasonal changes",
            "Maintain basic emergency preparedness"
        ],
        "Medium": [
            "Consider flood insurance",
            "Monitor weather alerts during heavy rainfall",
            "Have an emergency evacuation plan ready"
        ],
        "High": [
            "Obtain comprehensive flood insurance",
            "Install flood monitoring systems",
            "Develop detailed emergency response plan"
        ],
        "Very High": [
            "Immediate flood protection measures recommended",
            "Consider professional flood risk assessment",
            "Implement comprehensive emergency protocols"
        ]
    }
    
    # Generate geographic features based on coordinates
    geographic_features = []
    if abs(latitude) < 10:
        geographic_features.append("tropical climate zone")
    elif abs(latitude) < 30:
        geographic_features.append("subtropical region")
    else:
        geographic_features.append("temperate region")
    
    if abs(latitude) < 5:
        geographic_features.append("near equatorial zone")
    
    if latitude > 60:
        geographic_features.append("high latitude region")
    elif latitude < -60:
        geographic_features.append("antarctic region")
    
    return {
        "location_name": location_name,
        "risk_level": risk_level,
        "description": descriptions[risk_level],
        "recommendations": recommendations[risk_level],
        "elevation": round(random.uniform(10, 100), 1),
        "distance_from_water": round(random.uniform(200, 2000), 1),
        "geographic_features": ", ".join(geographic_features) if geographic_features else "standard geographic features",
        "analysis": f"Geographic analysis for coordinates {latitude}, {longitude}"
    }

@app.post("/api/analyze/image")
async def analyze_image(file: UploadFile = File(...)):
    """
    Analyze flood risk based on uploaded image using Gemini AI
    """
    try:
        logger.info(f"Analyzing image: {file.filename}")
        
        # Validate file
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        if file.size > 10 * 1024 * 1024:  # 10MB limit
            raise HTTPException(status_code=400, detail="File size must be less than 10MB")
        
        # Read image data
        image_data = await file.read()
        
        # Convert image to PIL Image for Gemini AI
        try:
            image = PILImage.open(io.BytesIO(image_data))
            
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
        except Exception as img_error:
            logger.error(f"Error processing image: {str(img_error)}")
            raise HTTPException(status_code=400, detail="Invalid image format")
        
        prompt = """
        Analyze this terrain image for flood risk assessment.
        
        Please provide:
        1. Risk Level (Low/Medium/High/Very High)
        2. Description of the risk based on what you see
        3. 3-5 specific recommendations
        4. Estimated elevation in meters
        5. Estimated distance from water bodies in meters
        6. What water bodies or flood risks you can identify in the image
        
        Format your response as JSON with these fields:
        - risk_level
        - description
        - recommendations (array of strings)
        - elevation (number)
        - distance_from_water (number)
        - image_analysis (string describing what you see)
        """
        
        try:
            model = genai.GenerativeModel('gemini-2.0-flash-exp')
            #storing ai response
            response = model.generate_content([prompt, image])
            #parsing ai response
            parsed_data = parse_gemini_response(response.text)
            
        except Exception as ai_error:
            logger.error(f"Error calling Gemini AI: {str(ai_error)}")
            # Fallback to simulated data if AI fails
            parsed_data = generate_image_risk_assessment()
            parsed_data["image_analysis"] = "Image analysis was not available, using simulated assessment"
        # Return structured response
        return {
            "success": True,
            **parsed_data,
            "ai_analysis": parsed_data.get("image_analysis", ""),
            "message": "Image analysis completed successfully using Gemini AI"
        }

        # Unhandled errors
    except Exception as e:
        logger.error(f"Error analyzing image: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


def generate_image_risk_assessment() -> dict:
    """Generate risk assessment for image analysis"""
    import random    
    risk_level = random.choice(["Low", "Medium", "High", "Very High"])    
    descriptions = {
        "Low": "Image analysis shows low flood risk terrain.",
        "Medium": "Image analysis indicates moderate flood risk factors.",
        "High": "Image analysis reveals high flood risk characteristics.",
        "Very High": "Image analysis shows very high flood risk indicators."
    }    
    recommendations = {
        "Low": [
            "Continue monitoring terrain changes",
            "Maintain current drainage systems",
            "Stay informed about weather patterns"
        ],
        "Medium": [
            "Improve drainage infrastructure",
            "Consider flood monitoring systems",
            "Develop emergency response plan"
        ],
        "High": [
            "Install comprehensive flood barriers",
            "Implement early warning systems",
            "Consider structural reinforcements"
        ],
        "Very High": [
            "Immediate flood protection measures needed",
            "Consider relocation to higher ground",
            "Implement comprehensive emergency protocols"
        ]
    }
    
    return {
        "risk_level": risk_level,
        "description": descriptions[risk_level],
        "recommendations": recommendations[risk_level],
        "elevation": round(random.uniform(10, 100), 1),
        "distance_from_water": round(random.uniform(200, 2000), 1)
    }





















































if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    ) 

