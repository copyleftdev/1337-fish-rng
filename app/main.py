from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
import jwt
import logging
import asyncio  

from .config import settings
from .schemas import Token, RandomNumber
from .video_processor import process_video, get_stream_url
from .dependencies import get_settings

app = FastAPI(title="Fish-Based RNG API",
              description="This API uses live video feed of fish movement to generate random numbers and secure tokens.",
              version="1.0.0")

@app.get("/generate_random", response_model=RandomNumber)
async def generate_random():
    stream_url = get_stream_url(settings.stream_url)
    result, random_number = await asyncio.to_thread(process_video, stream_url)
    if random_number is None:
        raise HTTPException(status_code=503, detail=result['error'])
    return result

@app.get("/generate_token", response_model=Token)
async def generate_token():
    stream_url = get_stream_url(settings.stream_url)
    _, random_number = await asyncio.to_thread(process_video, stream_url)
    if random_number is None:
        raise HTTPException(status_code=503, detail="Failed to generate random number.")
    
    payload = {
        "random_number": random_number,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)
    return {"token": token}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
