import random
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import Message
from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ᴢᴏᴅɪᴀᴋ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴢᴏᴅɪᴀᴋ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴢᴏᴅɪᴀᴋ</code> [ɴᴀᴍᴀ ᴢᴏᴅɪᴀᴋ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴇʀᴀᴡᴀɴɢ ʀᴀᴍᴀʟᴀɴ ᴢᴏᴅɪᴀᴋ ᴀɴᴅᴀ.</blockquote>
"""

@PY.UBOT("zodiak")
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<blockquote><b>**ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ:** <code>/ᴢᴏᴅɪᴀᴋ</code> [ᴛᴀᴜʀᴜs]\n\nᴄᴏɴᴛᴏʜ: <code>/ᴢᴏᴅɪᴀᴋ ᴛᴀᴜʀᴜs</code></b></blockquote>")

    a = " ".join(message.command[1:])
    api_url = f"https://api.siputzx.my.id/api/primbon/zodiak?zodiak={a}"

    try:
        response = requests.get(api_url).json()

        if response.get("status"):
            zodiak_res = response["data"]["zodiak"].upper()
            nomor_res = response["data"]["nomor_keberuntungan"]
            aroma_res = response["data"]["aroma_keberuntungan"]
            planet_res = response["data"]["planet_yang_mengitari"]
            bunga_res = response["data"]["bunga_keberuntungan"]
            warna_res = response["data"]["warna_keberuntungan"]
            batu_res = response["data"]["batu_keberuntungan"]
            elemen_res = response["data"]["elemen_keberuntungan"]
            pasangan_res = response["data"]["pasangan_zodiak"]
            
            reply_text = (
                f"<blockquote><emoji id=5080331039922980916>⚡️</emoji> ᴢᴏᴅɪᴀᴋ :\n <b>{zodiak_res}</b></blockquote>\n"
                f"<blockquote><emoji id=5787363840316411387>🗄</emoji> ɴᴏᴍᴏʀ ᴋᴇʙᴇʀᴜɴᴛᴜɴɢᴀɴ :\n {nomor_res}</blockquote>\n"
                f"<blockquote><emoji id=5787363840316411387>🗄</emoji> ᴀʀᴏᴍᴀ ᴋᴇʙᴇʀᴜɴᴛᴜɴɢᴀɴ :\n {aroma_res}</blockquote>\n"
                f"<blockquote><emoji id=5787363840316411387>🗄</emoji> ᴘʟᴀɴᴇᴛ ᴋᴇʙᴇʀᴜɴᴛᴜɴɢᴀɴ :\n {planet_res}</blockquote>\n"
                f"<blockquote><emoji id=5787363840316411387>🗄</emoji> ʙᴜɴɢᴀ ᴋᴇʙᴇʀᴜɴᴛᴜɴɢᴀɴ :\n {bunga_res}</blockquote>\n"
                f"<blockquote><emoji id=5787363840316411387>🗄</emoji> ᴡᴀʀɴᴀ ᴋᴇʙᴇʀᴜɴᴛᴜɴɢᴀɴ :\n {warna_res}</blockquote>\n"
                f"<blockquote><emoji id=5787363840316411387>🗄</emoji> ʙᴀᴛᴜ ᴋᴇʙᴇʀᴜɴᴛᴜɴɢᴀɴ :\n {batu_res}</blockquote>\n"
                f"<blockquote><emoji id=5787363840316411387>🗄</emoji> ᴇʟᴇᴍᴇɴ ᴋᴇʙᴇʀᴜɴᴛᴜɴɢᴀɴ :\n {elemen_res}</blockquote>\n"
                f"<blockquote><emoji id=5787363840316411387>🗄</emoji> ᴘᴀsᴀɴɢᴀɴ ᴢᴏᴅɪᴀᴋ :\n {pasangan_res}</blockquote>"
            )

            await message.reply_text(reply_text)
        else:
            await message.reply_text(f"<blockquote><b>❌ ᴍᴀᴀꜰ, ᴅᴀᴛᴀ ᴢᴏᴅɪᴀᴋ ᴜɴᴛᴜᴋ **{a}** ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
    except Exception as e:
        await message.reply_text(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ sᴀᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ:\n`{str(e)}`</b></blockquote>")
        
        
