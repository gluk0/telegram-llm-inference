import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from src.data.wallet import WalletHistoryFetcher

logger = logging.getLogger(__name__)

class TelegramBot:
    """Class to handle Telegram bot functionality."""
    
    def __init__(self, telegram_token: str, moralis_token: str):
        """Initialize the Telegram bot.
        
        Args:
            telegram_token: Telegram bot token
            moralis_token: Moralis API token
        """
        self.telegram_token = telegram_token
        self.moralis_token = moralis_token
        self.application = None
        self.wallet_history = WalletHistoryFetcher(moralis_token)
        
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
            wallet_address = "0xaD9e0d62f3945899eDf58050d27b077D6DBBd3Ba"
            
            history = await self.wallet_history.get_wallet_history(wallet_address)
            
            if not history:
                await update.message.reply_text(
                    "No wallet history available at the moment."
                )
                return
            
            # Format the wallet history into a readable message
            message = f"📊  Wallet History for {wallet_address[:6]}...{wallet_address[-4:]}:\n\n"
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
        self.application = Application.builder().token(self.telegram_token).build()
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("wallet", self.wallet))

    def run(self) -> None:
        """Run the bot."""
        if not self.application:
            self.setup()
        self.application.run_polling(allowed_updates=Update.ALL_TYPES) 