# Setup Guide

This guide will help you set up and run the Telegram LLM Inference bot.

## Prerequisites

- Python 3.9 or higher
- Poetry (Python dependency manager)
- Git

## API Keys Required

1. **Telegram Bot Token**
   - Go to [@BotFather](https://t.me/BotFather) on Telegram
   - Send `/newbot` command
   - Follow the prompts to create your bot
   - Save the API token provided

2. **Moralis API Token**
   - Create an account at [Moralis](https://moralis.io/)
   - Navigate to the Web3 APIs section
   - Generate a new API key
   - Save the API key

## Installation Steps

1. **Install Poetry** (if not already installed)
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd telegram-llm-inference
   ```

3. **Install Dependencies with Poetry**
   ```bash
   poetry install
   ```

4. **Configure Environment Variables**
   
   Create a `.env` file in the root directory:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   MORALIS_API_TOKEN=your_moralis_api_token_here
   ```

## Running the Bot

1. **Start the Bot**
   ```bash
   poetry run python src/main.py
   ```

2. **Verify the Bot is Running**
   - Open Telegram
   - Search for your bot using its username
   - Send the `/start` command
   - The bot should respond with a welcome message

## Available Commands

- `/start` - Initialize the bot and get welcome message
- `/wallet` - Query wallet history and transactions

## Troubleshooting

1. **Bot Not Responding**
   - Verify your Telegram Bot Token is correct
   - Check if the bot is running in your terminal
   - Ensure your internet connection is stable

2. **Wallet Queries Failed**
   - Verify your Moralis API Token is correct
   - Check the logs for specific error messages
   - Ensure you haven't exceeded Moralis API rate limits

## Logging

The bot logs important events and errors to help with debugging:
- Info logs: Basic operation information
- Error logs: Details about failed operations

Logs can be found in the application's output.
