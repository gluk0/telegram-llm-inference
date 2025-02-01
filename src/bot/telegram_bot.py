import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from src.data.wallet import WalletHistory

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
        self.wallet_history = WalletHistory()
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle the /start command.
        
        Args:
            update: The update from Telegram
            context: The context from the handler
        """
        user = update.message.from_user
        logger.info("User %s started the bot", user.first_name)
        await update.message.reply_text(
            "Hi! I'm a bot - Use /wallet to query a wallet address!"
        )

    async def wallet(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle the /wallet command.
        
        Args:
            update: The update from Telegram
            context: The context from the handler
        """
        user = update.message.from_user
        logger.info("User %s asked a wallet query", user.first_name)
        
        try:
            # Fetch wallet history
            history = await self.wallet_history.fetch_history()
            
            if not history:
                await update.message.reply_text(
                    "No wallet history available at the moment."
                )
                return
            
            # Format the wallet history into a readable message
            message = "📊 Your Wallet History:\n\n"
            for transaction in history:
                message += f"💰 Amount: {transaction['amount']}\n"
                message += f"📅 Date: {transaction['date']}\n"
                message += f"📝 Description: {transaction['description']}\n"
                message += "-------------------\n"
            
            await update.message.reply_text(message)
            
        except Exception as e:
            logger.error(f"Error fetching wallet history: {str(e)}")
            await update.message.reply_text(
                "Sorry, I couldn't fetch your wallet history at the moment. Please try again later."
            )

    def setup(self) -> None:
        """Set up the bot with handlers."""
        self.application = Application.builder().token(self.token).build()
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("wallet", self.wallet))

    def run(self) -> None:
        """Run the bot."""
        if not self.application:
            self.setup()
        self.application.run_polling(allowed_updates=Update.ALL_TYPES) 