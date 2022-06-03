import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "Jobboard"
    PROJECT_VERSION: str = "0.1.1"

    POSTGRESS_USER: str = os.getenv('POSTGRESS_USER')
    POSTGRESS_PASSWORD: str = os.getenv('POSTGRESS_PASSWORD')
    POSTGRESS_SERVER: str = os.getenv('POSTGRESS_SERVER')
    POSTGRESS_PORT: str = os.getenv('POSTGRESS_PORT')
    POSTGRESS_DB: str = os.getenv('POSTGRESS_DB')
    DATABASE_URL = f'postgresql://{POSTGRESS_USER}:{POSTGRESS_PASSWORD}@{POSTGRESS_SERVER}:{POSTGRESS_PORT}/{POSTGRESS_DB}'


settings = Settings()
