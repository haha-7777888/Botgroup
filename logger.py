from pyrogram import Client
from config import LOGGER_ID

async def log_event(client: Client, text: str):
    try:
        await client.send_message(LOGGER_ID, text)
    except Exception as e:
        print(f"Logger Error: {e}")
