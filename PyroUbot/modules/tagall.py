import asyncio
import random
from random import shuffle
from PyroUbot import *

__MODULE__ = "ᴛᴀɢᴀʟʟ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴀɢᴀʟʟ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴛᴀɢᴀʟʟ</code> [ᴘᴇsᴀɴ]
ᚗ <code>{0}ʙᴀᴛᴀʟ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴛᴀɢ ᴋᴇ sᴇʟᴜʀᴜʜ ᴀɴɢɢᴏᴛᴀ ɢʀᴜᴘ ᴅᴇɴɢᴀɴ ᴇᴍᴏᴊɪ ᴀᴄᴀᴋ.</blockquote>
"""

tagallgcid = []

emoji_categories = {
    "smileys": ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😍", "🥰", "😘", "😎", "🥳", "😇", "🙃", "😋", "😛", "🤪"],
    "animals": ["🐶", "🐱", "🐰", "🐻", "🐼", "🦁", "🐸", "🦊", "🦔", "🦄", "🐢", "🐠", "🐦", "🦜", "🦢", "🦚", "🦓", "🐅"],
    "food": ["🍎", "🍕", "🍔", "🍟", "🍩", "🍦", "🍓", "🥪", "🍣", "🍝", "🍤", "🥗", "🥐", "🍪", "🍰", "🍫", "🥤"],
    "nature": ["🌲", "🌺", "🌞", "🌈", "🌊", "🌍", "🍁", "🌻", "🌸", "🌴", "🌵", "🍃", "🍂", "🌼", "🌱", "🌾", "🍄"],
    "travel": ["✈️", "🚀", "🚲", "🚗", "⛵", "🏔️", "🚁", "🚂", "🏍️", "🚢", "🚆", "🛴", "🛸", "🛶", "🚟", "🚈", "🛵"],
    "sports": ["⚽", "🏀", "🎾", "🏈", "🎱", "🏓", "🥊", "⛳", "🏋️", "🏄", "🤸", "🏹", "🥋", " skateboard", "🎯", "🏆"],
    "music": ["🎵", "🎶", "🎤", "🎧", "🎼", "🎸", "🥁", "🎷", "🎺", "🎻", "🪕", "🎹", "🔊"],
    "celebration": ["🎉", "🎊", "🥳", "🎈", "🎁", "🍰", "🧁", "🥂", "🍾", "🎆", "🎇"],
    "work": ["💼", "👔", "👓", "📚", "✏️", "📆", "🖥️", "🖊️", "📂", "📌", "📎"],
    "emotions": ["❤️", "💔", "😢", "😭", "😠", "😡", "😊", "😃", "🙄", "😳", "😇", "😍"],
}

def emoji_random():
    random_category = random.choice(list(emoji_categories.keys()))
    return random.choice(emoji_categories[random_category])

@PY.UBOT("tagall")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    if message.chat.id in tagallgcid:
        return
    
    tagallgcid.append(message.chat.id)
    text = message.text.split(None, 1)[1] if len(message.text.split()) != 1 else ""
    
    users = [
        f"<a href=tg://user?id={member.user.id}>{emoji_random()}</a>"
        async for member in message.chat.get_members()
        if not (member.user.is_bot or member.user.is_deleted)
    ]
    shuffle(users)
    
    m = message.reply_to_message or message
    for output in [users[i : i + 5] for i in range(0, len(users), 5)]:
        if message.chat.id not in tagallgcid:
            break
        await m.reply_text(
            f"<blockquote>{text}</blockquote>\n\n{' '.join(output)}", 
            quote=bool(message.reply_to_message)
        )
        await asyncio.sleep(1.5)
        
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass

@PY.UBOT("batal")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    
    if message.chat.id not in tagallgcid:
        return await message.reply_text(
            f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇʀɪɴᴛᴀʜ ᴛᴀɢᴀʟʟ ʏᴀɴɢ sᴇᴅᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ.</b></blockquote>"
        )
    
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass
    await message.reply_text(f"<blockquote><b>{brhsl} ᴛᴀɢᴀʟʟ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴀᴛᴀʟᴋᴀɴ!</b></blockquote>")
    