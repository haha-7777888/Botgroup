from pyrogram import Client
from config import LOGGER_ID

async def log_event(client: Client, text: str):
    print(f"🔍 [LOGGER DEBUG] Trying to send log to ID: {LOGGER_ID}")
    try:
        await client.send_message(LOGGER_ID, text)
        print("✅ [LOGGER DEBUG] Log sent successfully!")
    except Exception as e:
        print(f"❌ [LOGGER ERROR FAILED]: {e}")
