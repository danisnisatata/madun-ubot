import os
import requests
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ᴀᴛᴛᴘ-ᴛᴛᴘ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴛᴛᴘ-ᴛᴛᴘ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴀᴛᴛᴘ</code> [ᴛᴇᴋs] : ʙᴜᴀᴛ sᴛɪᴄᴋᴇʀ ᴛᴇᴋs ʙᴇʀᴡᴀʀɴᴀ (ᴀɴɪᴍᴀsɪ).
ᚗ <code>{0}ᴛᴛᴘ</code> [ᴛᴇᴋs] : ʙᴜᴀᴛ sᴛɪᴄᴋᴇʀ ᴛᴇᴋs ʙɪᴀsᴀ.

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴜʙᴀʜ ᴛᴇᴋs ᴍᴇɴᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ ᴋᴇʀᴇɴ sᴇᴄᴀʀᴀ ɪɴsᴛᴀɴ ᴍᴇʟᴀʟᴜɪ ᴀᴘɪ.</blockquote>
"""

API_KEY = "@iqbalnew77"

@PY.UBOT("attp")
@PY.TOP_CMD
async def attp(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    jalan = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴀᴛᴛᴘ...</b></blockquote>")
    
    try:
        args = get_arg(message)
        if not args:
            return await jalan.edit(f"<blockquote><b>{ggl} ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇᴋs!\nᴄᴏɴᴛᴏʜ: <code>.ᴀᴛᴛᴘ</code> ɪǫʙᴀʟ</b></blockquote>")
        
        text = args
        url = f"https://api.botcahx.eu.org/api/maker/attp?text={text}&apikey={API_KEY}"
        
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file_path = "attp.webp"
            with open(file_path, "wb") as file:
                file.write(response.content)
            
            await client.send_sticker(
                chat_id=message.chat.id,
                sticker=file_path,
                reply_to_message_id=message.id
            )
            await jalan.delete()
            if os.path.exists(file_path):
                os.remove(file_path)
        else:
            await jalan.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ sᴛɪᴄᴋᴇʀ ᴀᴛᴛᴘ.</b></blockquote>")
    except Exception as e:
        await jalan.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("ttp")
@PY.TOP_CMD
async def ttp(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    jalan = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴛᴛᴘ...</b></blockquote>")
    
    try:
        args = get_arg(message)
        if not args:
            return await jalan.edit(f"<blockquote><b>{ggl} ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇᴋs!\nᴄᴏɴᴛᴏʜ: <code>.ᴛᴛᴘ</code> ɪǫʙᴀʟ</b></blockquote>")
        
        text = args
        url = f"https://api.botcahx.eu.org/api/maker/ttp?text={text}&apikey={API_KEY}"
        
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file_path = "ttp.webp"
            with open(file_path, "wb") as file:
                file.write(response.content)
            
            await client.send_sticker(
                chat_id=message.chat.id,
                sticker=file_path,
                reply_to_message_id=message.id
            )
            await jalan.delete()
            if os.path.exists(file_path):
                os.remove(file_path)
        else:
            await jalan.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ sᴛɪᴄᴋᴇʀ ᴛᴛᴘ.</b></blockquote>")
    except Exception as e:
        await jalan.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        
