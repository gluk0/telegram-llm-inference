"""Configuration settings module."""
import os
from dotenv import load_dotenv

load_dotenv()

# Bot settings
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MORALIS_API_KEY = os.getenv("MORALIS_API_KEY")

# Logging settings
LOGGING_CONFIG = {
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "level": "INFO"
} 