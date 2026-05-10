import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "sᴛᴀʟᴋᴛᴛ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀʟᴋᴛᴛ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴛᴀʟᴋᴛᴛ</code> [ᴜsᴇʀɴᴀᴍᴇ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟɪʜᴀᴛ ɪɴꜰᴏʀᴍᴀsɪ ᴘʀᴏꜰɪʟ ᴛɪᴋᴛᴏᴋ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ.</blockquote>
"""

@PY.UBOT("stalktt")
@PY.TOP_CMD
async def stalktt(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏʀᴍᴀsɪ...</b></blockquote>")
    
    if len(message.command) < 2:
        return await jalan.edit(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ ᴛɪᴋᴛᴏᴋ!</b></blockquote>")
    
    username_target = message.command[1]
    url = f"https://api.betabotz.eu.org/api/stalk/tt?username={username_target}&apikey=@iqbalnew77"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get('result'):
                hasil = data['result']
                
                caption = f"""
<blockquote><b>⦪ ɪɴꜰᴏ ᴘʀᴏꜰɪʟ ᴛɪᴋᴛᴏᴋ ⦫</b>

<b>ᚗ ᴜsᴇʀɴᴀᴍᴇ :</b> <code>{hasil['username']}</code>
<b>ᚗ ᴅᴇsᴋ :</b> <code>{hasil.get('description', 'ᴛɪᴅᴀᴋ ᴀᴅᴀ')}</code>
<b>ᚗ sᴜᴋᴀ :</b> <code>{hasil['likes']}</code>
<b>ᚗ ᴘᴇɴɢɪᴋᴜᴛ :</b> <code>{hasil['followers']}</code>
<b>ᚗ ᴅɪɪᴋᴜᴛɪ :</b> <code>{hasil['following']}</code>
<b>ᚗ ᴘᴏsᴛɪɴɢ :</b> <code>{hasil['totalPosts']}</code></blockquote>
"""
                photo_url = hasil['profile']
                photo_path = wget.download(photo_url)
                
                await client.send_photo(
                    message.chat.id, 
                    photo=photo_path, 
                    caption=caption
                )
                
                if os.path.exists(photo_path):
                    os.remove(photo_path)
                
                await jalan.delete()
            else:
                await jalan.edit(f"<blockquote><b>{ggl} ᴅᴀᴛᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
        else:
            await jalan.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ. sᴛᴀᴛᴜs: {response.status_code}</b></blockquote>")
    
    except Exception as e:
        await jalan.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        