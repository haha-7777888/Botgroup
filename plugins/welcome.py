from pyrogram import Client, enums
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from logger import log_event

@Client.on_chat_member_updated()
async def welcome_handler(client: Client, chat_member: ChatMemberUpdated):
    # Pyrogram ဗားရှင်းအမျိုးမျိုးအတွက် အဆင်ပြေစေရန် safety check ပြုလုပ်ခြင်း
    new_m = getattr(chat_member, "new_chat_member", None) or getattr(chat_member, "new_member", None)
    old_m = getattr(chat_member, "old_chat_member", None) or getattr(chat_member, "old_member", None)
    
    if not new_m:
        return

    chat = chat_member.chat
    user = new_m.user

    # ၁။ Bot ကို Group တွင် Admin ပေးလိုက်သည့်အခါ (သို့) ထည့်လိုက်သည့်အခါ
    if user.id == client.me.id:
        # ရှေးဦးစွာ member ဖြစ်နေပြီးမှ admin ဖြစ်သွားခြင်း ဟုတ်မဟုတ် စစ်ဆေးရန်
        if old_m and old_m.status in [enums.ChatMemberStatus.MEMBER, enums.ChatMemberStatus.RESTRICTED]:
            return
        
        added_by = chat_member.from_user
        
        log_text = (
            f"📥 <b>Bot Add Group Info</b>\n\n"
            f"🏷 Name: {chat.title}\n"
            f"🆔 ID: <code>{chat.id}</code>\n"
            f"👤 ထည့်သွင်းပေးသူ: {added_by.first_name if added_by else 'Unknown'} (<code>{added_by.id if added_by else 'N/A'}</code>)"
        )
        await log_event(client, log_text)
        return

    # ၂။ Group ထဲသို့ Member အသစ်တစ်ဦး ဝင်လာသည့်အခါ (Welcome မက်ဆေ့ချ် ပို့ရန်)
    if new_m.status in [enums.ChatMemberStatus.MEMBER, enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
        # Bot ဝင်လာတာကို ကျော်ရန်
        if user.is_bot:
            return

        user_mention = f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
        
        welcome_text = (
            f"<b>{chat.title}</b>\n\n"
            f"<tg-emoji emoji-id='6120837741266603661'>🎧</tg-emoji><b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ</b><tg-emoji emoji-id='6267119710278522544'>🎧</tg-emoji> {user_mention}\n\n"
            f"<tg-emoji emoji-id='6264538349034281099'>🎧</tg-emoji><b>ɴᴀᴍᴇ</b><tg-emoji emoji-id='6267119710278522544'>🎧</tg-emoji>{user_mention}\n\n"
            f"<tg-emoji emoji-id='6030656587830399914'>🎧</tg-emoji><b>ID</b><tg-emoji emoji-id='6267119710278522544'>🎧</tg-emoji><code>{user.id}</code>\n\n"
            f"<tg-emoji emoji-id='4972172205652706288'>🎧</tg-emoji><tg-emoji emoji-id='4974451085235192775'>🎧</tg-emoji><tg-emoji emoji-id='4972061468510913587'>🎧</tg-emoji><tg-emoji emoji-id='4972370753400865760'>🎧</tg-emoji><tg-emoji emoji-id='4972135526631999147'>🎧</tg-emoji>"
        )
        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💞", url="https://t.me/your_channel")]
        ])
        
        try:
            await client.send_message(
                chat.id, 
                welcome_text, 
                reply_markup=keyboard, 
                parse_mode=enums.ParseMode.HTML
            )
        except Exception as e:
            print(f"Welcome Member Error: {e}")
