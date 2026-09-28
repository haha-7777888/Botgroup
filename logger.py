from pyrogram import Client
from config import OWNER_ID

async def log_event(client: Client, text: str):
    try:
        await client.send_message(OWNER_ID, text)
    except Exception as e:
        print(f"Logger Error: {e}")
