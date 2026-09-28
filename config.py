import os

API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))  


LOGGER_ID = int(os.getenv("LOGGER_ID", "-1001234567890")) 

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/your_channel")
GROUP_LINK = os.getenv("GROUP_LINK", "https://t.me/your_group")
