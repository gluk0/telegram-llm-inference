#!/usr/bin/env python
import logging
from src.config.settings import TELEGRAM_BOT_TOKEN, MORALIS_API_KEY, LOGGING_CONFIG
from src.bot.telegram_bot import TelegramBot

logging.basicConfig(**LOGGING_CONFIG)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

def main() -> None:
    bot = TelegramBot(TELEGRAM_BOT_TOKEN, MORALIS_API_KEY)
    bot.run()

if __name__ == "__main__":
    main()