telegram-llm-inference
===================

A simple telegram bot that uses a LLM to generate responses to messages from a public LLM API, transforming data from the LLM API into a more user-friendly format for telegram consumption. 

Key Components:
-------------
- Main bot runner (src/main.py)
- Bot implementation (src/bot/telegram_bot.py)
- Configuration management (src/config/settings.py)

Requirements:
------------
- Python 3.7+
- Telegram Bot Token
- Required Python packages (see requirements.txt)

To run the bot:
--------------
1. Set up your environment variables (TELEGRAM_BOT_TOKEN)
2. Install dependencies from requirements.txt
3. Run: python src/main.py

Structure: 
----------
```
├── src/
│ ├── bot/
│ │ └── telegram_bot.py
│ ├── config/
│ │ └── settings.py
│ └── main.py
├── requirements.txt
└── README.md
```