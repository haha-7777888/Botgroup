from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHANNEL, GROUP_LINK, OWNER_ID
from logger import log_event

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    print("👉 [START DEBUG] /start command received from user:", message.from_user.id)
    user = message.from_user
    
    log_text = (
        f"🤖 **Bot Start info**\n\n"
        f"👤 Name: {user.first_name}\n"
        f"🆔 ID: `{user.id}`\n"
        f"🔗 Username: @{user.username if user.username else 'None'}"
    )
    
    
    await log_event(client, log_text)

    text = (
        f"မင်္ဂလာပါ {user.first_name} 👋\n\n"
        f"ကျွန်တော်ကတော့ Group များကို အလိုအလျောက်ကြိုဆိုပေးသော Welcome Bot ဖြစ်ပါတယ်။"
    )
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Add me to your group", url=f"https://t.me/{client.me.username}?startgroup=true")],
        [InlineKeyboardButton("Channel", url=SUPPORT_CHANNEL),
        InlineKeyboardButton(" Support", url=GROUP_LINK)],
        [InlineKeyboardButton("Owner", url=f"tg://openmessage?user_id={OWNER_ID}")]
    ])
    
    await message.reply_text(text, reply_markup=keyboard)
