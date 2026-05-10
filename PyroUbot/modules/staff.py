import os
from PyroUbot import *

__MODULE__ = "sᴛᴀꜰꜰ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀꜰꜰ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴛᴀꜰꜰ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀꜰᴛᴀʀ ɪɴꜰᴏʀᴍᴀsɪ sᴇʟᴜʀᴜʜ sᴛᴀꜰꜰ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ.</blockquote>
"""

@PY.UBOT("staff")
@PY.TOP_CMD
async def staff_cmd(client, message):
    chat_title = message.chat.title
    creator = []
    co_founder = []
    admin = []
    
    async for x in message.chat.get_members():
        full_name = f"{x.user.first_name} {x.user.last_name or ''}"
        mention = f"<a href=tg://user?id={x.user.id}>{full_name}</a>"
        
        if (
            x.status.value == "administrator"
            and x.privileges
            and x.privileges.can_promote_members
        ):
            if x.custom_title:
                co_founder.append(f" ┣ {mention} - <i>{x.custom_title}</i>")
            else:
                co_founder.append(f" ┣ {mention}")
        elif x.status.value == "administrator":
            if x.custom_title:
                admin.append(f" ┣ {mention} - <i>{x.custom_title}</i>")
            else:
                admin.append(f" ┣ {mention}")
        elif x.status.value == "owner":
            if x.custom_title:
                creator.append(f" ┗ {mention} - <b>{x.custom_title}</b>")
            else:
                creator.append(f" ┗ {mention}")

    res = f"<b>sᴛᴀꜰꜰ ɢʀᴜᴘ</b>\n<b>{chat_title}</b>\n"
    
    if creator:
        res += f"\n<emoji id=5803032306213982905>👑</emoji> <b>ᴏᴡɴᴇʀ :</b>\n{creator[0]}\n"
        
    if co_founder:
        co_founder[-1] = co_founder[-1].replace("┣", "┗")
        res += f"\n<emoji id=5800942688660360834>👮</emoji> <b>ᴄᴏ-ꜰᴏᴜɴᴅᴇʀ :</b>\n" + "\n".join(co_founder) + "\n"
        
    if admin:
        admin[-1] = admin[-1].replace("┣", "┗")
        res += f"\n<emoji id=5260271509158501258>👮</emoji> <b>ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ :</b>\n" + "\n".join(admin)

    await message.reply(f"<blockquote>{res}</blockquote>")
    