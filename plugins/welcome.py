from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from logger import log_event

@Client.on_chat_member_updated()
async def welcome_new_admin(client: Client, chat_member: ChatMemberUpdated):
    # Bot ကို Admin ပေးလိုက်ချိန်ကို စစ်ဆေးခြင်း
    if chat_member.new_chat_member and chat_member.new_chat_member.user.id == client.me.id:
        if chat_member.old_chat_member and chat_member.old_chat_member.status in ["member", "restricted"]:
            return
        
        chat = chat_member.chat
        added_by = chat_member.from_user
        
        # ပုံမပါ၊ ပုံပါအတိုင်း Premium Emoji များနှင့် စာသား၊ ခလုတ် ၁ ခု
        welcome_text = (
            f"⚡ **WELCOME TO , {chat.title}**\n\n"
            f"👤 **NAME** » {added_by.first_name if added_by else 'Unknown'}\n"
            f"🆔 **ID** » `{added_by.id if added_by else 'N/A'}`\n"
            f"⏰ **STATUS** » Bot Successfully Added as Admin! 🫀ဦးစားရှာရန် နှိပ်ပါ"
        )
        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🫀 ဦးစားရှာရန် နှိပ်ပါ (1)", url="https://t.me/your_channel")]
        ])
        
        try:
            await client.send_message(chat.id, welcome_text, reply_markup=keyboard)
        except Exception as e:
            print(f"Welcome Error: {e}")

        # Logger သို့ Group အချက်အလက် ပို့ရန်
        log_text = (
            f"📥 **Bot အသစ်ထည့်ခံရသည့် Group**\n\n"
            f"နံမည်: {chat.title}\n"
            f"ID: `{chat.id}`\n"
            f"ထည့်သွင်းပေးသူ: {added_by.first_name if added_by else 'Unknown'} (`{added_by.id if added_by else 'N/A'}`)"
        )
        await log_event(client, log_text)
