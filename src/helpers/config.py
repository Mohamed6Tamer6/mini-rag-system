from pydantic_settings import BaseSettings, SettingsConfigDict 
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):

    APP_NAME : str
    VERSION_NAME : str

    model_config = SettingsConfigDict(env_file=str(BASE_DIR / ".env"))

def get_settings():
    return Settings()
