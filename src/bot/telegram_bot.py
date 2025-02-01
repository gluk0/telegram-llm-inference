"""Telegram bot module."""
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logger = logging.getLogger(__name__)

class TelegramBot:
    """Class to handle Telegram bot functionality."""
    
    def __init__(self, token: str):
        """Initialize the Telegram bot.
        
        Args:
            token: Telegram bot token
        """
        self.token = token
        self.application = None
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle the /start command.
        
        Args:
            update: The update from Telegram
            context: The context from the handler
        """
        user = update.message.from_user
        logger.info("User %s started the bot", user.first_name)
        await update.message.reply_text(
            "Hi! I'm a bot - Use /question to ask me something!"
        )

    async def question(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle the /question command.
        
        Args:
            update: The update from Telegram
            context: The context from the handler
        """
        user = update.message.from_user
        logger.info("User %s asked a question", user.first_name)
        await update.message.reply_text(
            "This is a basic response to your question!"
        )

    def setup(self) -> None:
        """Set up the bot with handlers."""
        self.application = Application.builder().token(self.token).build()
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("question", self.question))

    def run(self) -> None:
        """Run the bot."""
        if not self.application:
            self.setup()
        self.application.run_polling(allowed_updates=Update.ALL_TYPES) 