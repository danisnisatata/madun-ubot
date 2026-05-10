import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "sᴛᴀʟᴋɢʜ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀʟᴋɢʜ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴛᴀʟᴋɢʜ</code> [ᴜsᴇʀɴᴀᴍᴇ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟɪʜᴀᴛ ɪɴꜰᴏʀᴍᴀsɪ ᴘʀᴏꜰɪʟ ɢɪᴛʜᴜʙ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ.</blockquote>
"""

@PY.UBOT("stalkgh")
@PY.TOP_CMD
async def stalkgh(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏ ᴘʀᴏꜰɪʟ...</b></blockquote>")
    
    if len(message.command) < 2:
        return await jalan.edit(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ ɢɪᴛʜᴜʙ!</b></blockquote>")
    
    username_gh = message.command[1]
    url = f"https://api.betabotz.eu.org/api/stalk/github?username={username_gh}&apikey=@iqbalnew77"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get('result') and data['result'].get('user'):
                result = data['result']['user']
                # Menggunakan avatar GitHub asli jika tersedia, jika tidak pakai fallback
                photo_url = result.get('avatar') or "https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"
                
                caption = f"""
<blockquote><b>⦪ ɪɴꜰᴏ ᴘʀᴏꜰɪʟ ɢɪᴛʜᴜʙ ⦫</b>

<b>ᚗ ɴᴀᴍᴀ :</b> <code>{result.get('name', 'ᴛɪᴅᴀᴋ ᴀᴅᴀ')}</code>
<b>ᚗ ᴜsᴇʀɴᴀᴍᴇ :</b> <code>{result['username']}</code>
<b>ᚗ ᴘᴇɴɢɪᴋᴜᴛ :</b> <code>{result['followers']}</code>
<b>ᚗ ᴅɪɪᴋᴜᴛɪ :</b> <code>{result['following']}</code>
<b>ᚗ ʙɪᴏ :</b> <code>{result.get('bio', 'ᴛɪᴅᴀᴋ ᴀᴅᴀ')}</code>
<b>ᚗ ɪᴅ ᴜsᴇʀ :</b> <code>{result['idUser']}</code></blockquote>
"""
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
                await jalan.edit(f"<blockquote><b>{ggl} ᴅᴀᴛᴀ ᴘʀᴏꜰɪʟ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
        else:
            await jalan.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ. sᴛᴀᴛᴜs: {response.status_code}</b></blockquote>")
    
    except Exception as e:
        await jalan.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        