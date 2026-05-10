import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "sᴛᴀʟᴋʏᴛ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀʟᴋʏᴛ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴛᴀʟᴋʏᴛ</code> [ᴜsᴇʀɴᴀᴍᴇ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟɪʜᴀᴛ ɪɴꜰᴏʀᴍᴀsɪ ᴄʜᴀɴɴᴇʟ ʏᴏᴜᴛᴜʙᴇ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ.</blockquote>
"""

@PY.UBOT("stalkyt")
@PY.TOP_CMD
async def stalkyt(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ ɪɴꜰᴏʀᴍᴀsɪ...</b></blockquote>")
    
    if len(message.command) < 2:
        return await jalan.edit(f"<blockquote><b>{ggl} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ ʏᴛ!</b></blockquote>")
    
    username = message.command[1]
    url = f"https://api.betabotz.eu.org/api/stalk/yt?username={username}&apikey=@iqbalnew77"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get('result') and data['result'].get('data'):
                first_channel = data['result']['data'][0]
                photoUrl = first_channel['avatar']
                description = first_channel.get('description', 'ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴇsᴋʀɪᴘsɪ')
                
                caption = f"""
<blockquote><b>⦪ ɪɴꜰᴏ ᴄʜᴀɴɴᴇʟ ʏᴏᴜᴛᴜʙᴇ ⦫</b>

<b>ᚗ ɴᴀᴍᴀ :</b> <code>{first_channel['channelName']}</code>
<b>ᚗ sᴜʙs :</b> <code>{first_channel['subscriberH']}</code>
<b>ᚗ ᴅᴇsᴋ :</b> <code>{description}</code>
<b>ᚗ ᴛᴀᴜᴛᴀɴ :</b> <a href='{first_channel['url']}'>ᴋʟɪᴋ ᴅɪ sɪɴɪ</a></blockquote>
"""
                photo_path = wget.download(photoUrl)
                await client.send_photo(
                    message.chat.id, 
                    photo=photo_path, 
                    caption=caption
                )
                
                if os.path.exists(photo_path):
                    os.remove(photo_path)
                
                await jalan.delete()
            else:
                await jalan.edit(f"<blockquote><b>{ggl} ᴅᴀᴛᴀ ᴄʜᴀɴɴᴇʟ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
        else:
            await jalan.edit(f"<blockquote><b>{ggl} ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ. sᴛᴀᴛᴜs: {response.status_code}</b></blockquote>")
    
    except Exception as e:
        await jalan.edit(f"<blockquote><b>{ggl} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        