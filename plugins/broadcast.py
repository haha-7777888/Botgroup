import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID

# ရိုးရှင်းစေရန် Memory ထဲတွင် User နှင့် Group ID များ သိမ်းရန် Set သုံးထားသည် (Database သုံးလိုက ထည့်နိုင်သည်)
allowed_chats = set()

@Client.on_message(~filters.private & ~filters.bot)
async def track_chats(client: Client, message: Message):
    if message.chat:
        allowed_chats.add(message.chat.id)

@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_message(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("ကျေးဇူးပြု၍ Broadcast လုပ်လိုသည့် စာသားကို Reply လုပ်ပြီး ပို့ပါ။")
    
    query = message.reply_to_message
    sent_count = 0
    
    # Start လုပ်ထားသူများနှင့် Group အားလုံးထံ ပို့မည်
    all_targets = list(allowed_chats)
    
    for target in all_targets:
        try:
            await query.copy(chat_id=target)
            sent_count += 1
            await asyncio.sleep(0.2)
        except Exception:
            pass
            
    await message.reply_text(f"✅ Broadcast အောင်မြင်ပါသည်၊ Chat ပေါင်း {sent_count} ခုသို့ ပို့ပြီးပါပြီ။")
