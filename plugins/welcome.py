from pyrogram import Client, filters, enums
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from logger import log_event

@Client.on_chat_member_updated()
async def welcome_handler(client: Client, chat_member: ChatMemberUpdated):
    new_member = chat_member.new_member
    old_member = chat_member.old_member
    
    if not new_member:
        return

    
    if new_member.user.id == client.me.id:
        if old_member and old_member.status in ["member", "restricted"]:
            return
        
        chat = chat_member.chat
        added_by = chat_member.from_user
        
        
        log_text = (
            f"📥 <b>Bot အသစ်ထည့်ခံရသည့် Group</b>\n\n"
            f"🏷 နမည်: {chat.title}\n"
            f"🆔 ID: <code>{chat.id}</code>\n"
            f"👤 ထည့်သွင်းပေးသူ: {added_by.first_name if added_by else 'Unknown'} (<code>{added_by.id if added_by else 'N/A'}</code>)"
        )
        await log_event(client, log_text)
        return

    
    if new_member.status in [enums.ChatMemberStatus.MEMBER, enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
        if new_member.user.is_bot:
            return

        chat = chat_member.chat
        user = new_member.user
        
        
        user_mention = f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
        
        welcome_text = (
            f"<b>⚡ WELCOME TO , {chat.title}</b>\n\n"
            f"👤 <b>NAME</b> » {user_mention}\n"
            f"🆔 <b>ID</b> » <code>{user.id}</code>\n"
            f"⏰ <b>TIME</b> » Bot Successfully Added! <tg-emoji emoji-id='6289327805050134049'>🎧</tg-emoji> ရည်းစားရှာရန် နှိပ်ပါ (1)"
        )
        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💞 ရည်းစားရှာရန် နှိပ်ပါ (1)", url="https://t.me/your_channel")]
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
