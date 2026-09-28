from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHANNEL, GROUP_LINK, OWNER_ID
from logger import log_event

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    user = message.from_user
    
    # Logger သို့ ပို့ရန်
    log_text = (
        f"🤖 **Bot Start လုပ်သူ အချက်အလက်**\n\n"
        f"👤 အမည်: {user.first_name}\n"
        f"🆔 ID: `{user.id}`\n"
        f"🔗 Username: @{user.username if user.username else 'None'}"
    )
    await log_event(client, log_text)

    # Start မက်ဆေ့ချ်
    text = (
        f"မင်္ဂလာပါ {user.first_name} 👋\n\n"
        f"ကျွန်တော်ကတော့ Group များကို အလိုအလျောက်ကြိုဆိုပေးပြီး စီမံခန့်ခွဲပေးတဲ့ Welcome Bot ဖြစ်ပါတယ်။"
    )
    
    # ခလုတ် ၄ ခု ပါဝင်စေရန် ပြင်ဆင်ထားခြင်း
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add me to your group", url=f"https://t.me/{client.me.username}?startgroup=true")],
        [InlineKeyboardButton("📢 Group / Channel", url=SUPPORT_CHANNEL)],
        [InlineKeyboardButton("🌐 Support Group", url=GROUP_LINK)],
        [InlineKeyboardButton("👑 Owner", url=f"tg://openmessage?user_id={OWNER_ID}")]
    ])
    
    await message.reply_text(text, reply_markup=keyboard)
