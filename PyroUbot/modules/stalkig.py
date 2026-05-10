import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "sᴛᴀʟᴋɪɢ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀʟᴋɪɢ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴛᴀʟᴋɪɢ</code> [ᴜsᴇʀɴᴀᴍᴇ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟɪʜᴀᴛ ɪɴꜰᴏʀᴍᴀsɪ ᴘʀᴏꜰɪʟ ɪɴsᴛᴀɢʀᴀᴍ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ.</blockquote>
"""

@PY.UBOT("stalkig")
@PY.TOP_CMD
async def stalkig(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏ rᴏꜰɪʟ...</b></blockquote>")
    
    if len(message.command) < 2:
        return await jalan.edit(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ ɪɴsᴛᴀɢʀᴀᴍ!</b></blockquote>")
    
    username_ig = message.command[1]
    url = f"https://api.betabotz.eu.org/api/stalk/ig?username={username_ig}&apikey=@iqbalnew77"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get('result'):
                hasil = data['result']
                
                caption = f"""
<blockquote><b>⦪ ɪɴꜰᴏ ᴘʀᴏꜰɪʟ ɪɴsᴛᴀɢʀᴀᴍ ⦫</b>

<b>ᚗ ᴜsᴇʀɴᴀᴍᴇ :</b> <code>{hasil['username']}</code>
<b>ᚗ ɴᴀᴍᴀ :</b> <code>{hasil['fullName']}</code>
<b>ᚗ ᴘᴇɴɢɪᴋᴜᴛ :</b> <code>{hasil['followers']}</code>
<b>ᚗ ᴅɪɪᴋᴜᴛɪ :</b> <code>{hasil['following']}</code>
<b>ᚗ ᴘᴏsᴛɪɴɢ :</b> <code>{hasil['postsCount']}</code>
<b>ᚗ ʙɪᴏ :</b> <code>{hasil.get('bio', 'ᴛɪᴅᴀᴋ ᴀᴅᴀ')}</code></blockquote>
"""
                photo_path = wget.download(hasil['photoUrl'])
                await client.send_photo(
                    message.chat.id, 
                    photo=photo_path, 
                    caption=caption
                )
                
                if os.path.exists(photo_path):
                    os.remove(photo_path)
                
                await jalan.delete()
            else:
                await jalan.edit(f"<blockquote><b>{ggl} ᴅᴀᴛᴀ ᴘʀᴏꜰɪʟ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
        else:
            await jalan.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ. sᴛᴀᴛᴜs: {response.status_code}</b></blockquote>")
    
    except Exception as e:
        await jalan.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        