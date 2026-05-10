import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "sᴛᴀʟᴋꜰꜰ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀʟᴋꜰꜰ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴛᴀʟᴋꜰꜰ</code> [ɪᴅ ᴀᴋᴜɴ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏʀᴍᴀsɪ ᴀᴋᴜɴ ꜰʀᴇᴇ ꜰɪʀᴇ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ɪᴅ.</blockquote>
"""

@PY.UBOT("stalkff")
@PY.TOP_CMD
async def stalkff(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ɪᴅ...</b></blockquote>")
    
    if len(message.command) < 2:
        return await jalan.edit(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ɪᴅ ᴀᴋᴜɴ ꜰꜰ!</b></blockquote>")
    
    account_id = message.command[1]
    url = f"https://ff.lxonfire.workers.dev/?id={account_id}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            # Parsing data dari API
            nickname = data.get('nickname', 'ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ')
            region = data.get('region', 'ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ')
            openid = data.get('open_id', 'ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ')
            photo_url = data.get('img_url')
            
            caption = f"""
<blockquote><b>⦪ ɪɴꜰᴏ ᴀᴋᴜɴ ꜰʀᴇᴇ ꜰɪʀᴇ ⦫</b>

<b>ᚗ ɴɪᴄᴋɴᴀᴍᴇ :</b> <code>{nickname}</code>
<b>ᚗ ʀᴇɢɪᴏɴ :</b> <code>{region}</code>
<b>ᚗ ᴏᴘᴇɴ ɪᴅ :</b> <code>{openid}</code></blockquote>
"""
            if photo_url:
                photo_path = wget.download(photo_url)
                await client.send_photo(
                    message.chat.id, 
                    photo=photo_path, 
                    caption=caption
                )
                if os.path.exists(photo_path):
                    os.remove(photo_path)
            else:
                await message.reply(caption)
                
            await jalan.delete()
        else:
            await jalan.edit(f"<blockquote><b>{ggl} ᴅᴀᴛᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ᴀᴛᴀᴜ ᴀᴘɪ ᴇʀʀᴏʀ.</b></blockquote>")
    
    except Exception as e:
        await jalan.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        