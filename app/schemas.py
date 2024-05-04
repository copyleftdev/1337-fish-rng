# schemas.py
from pydantic import BaseModel

class Token(BaseModel):
    token: str
    class Config:
        schema_extra = {
            "example": {
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
            }
        }

class RandomNumber(BaseModel):
    random_number: int
    class Config:
        schema_extra = {
            "example": {
                "random_number": 42
            }
        }
