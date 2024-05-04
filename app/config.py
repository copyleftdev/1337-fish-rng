from pydantic_settings import BaseSettings
import os 

class Settings(BaseSettings):
    secret_key: str = os.getenv('TEST_SECRET', 'your_default_secret_key_here')
    algorithm: str = "HS256"
    stream_url: str = "https://www.youtube.com/watch?v=R34ot1LETK0"
    api_key: str = "neverdothisinproduction"

    class Config:
        env_file = ".env"

settings = Settings()
