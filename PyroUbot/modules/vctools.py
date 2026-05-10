import os
import wget
import math
import asyncio
from datetime import timedelta
from time import time
from functools import partial
from yt_dlp import YoutubeDL
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
from pytgcalls.types.calls import Call
from pytgcalls.exceptions import NotInCallError
from youtubesearchpython import VideosSearch
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
from pyrogram.errors import ChatAdminRequired, UserBannedInChannel, FloodWait, MessageNotModified
from PyroUbot import *

__MODULE__ = "ᴠᴄᴛᴏᴏʟꜱ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟꜱ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴊᴠᴄ</code> → ᴜɴᴛᴜᴋ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ.
ᚗ <code>{0}ʟᴠᴄ</code> → ᴜɴᴛᴜᴋ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ.

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴇʟᴏʟᴀ ᴋᴇʜᴀᴅɪʀᴀɴ ᴜʙᴏᴛ ᴅɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.</blockquote>
"""

@PY.UBOT("lvc")
@PY.TOP_CMD
@PY.GROUP
async def leave_vc(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    
    mex = await message.reply(f"<blockquote><b>{prs} ᴘʀᴏᴄᴇssɪɴɢ...</b></blockquote>")
    try:
        await client.call_py.leave_call(message.chat.id)
        await mex.edit(f"<blockquote><b>{brhsl} ʙᴇʀʜᴀsɪʟ ᴛᴜʀᴜɴ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ.</b></blockquote>")
    except NotInCallError:
        await mex.edit(f"<blockquote><b>{ggl} ᴀɴᴅᴀ ʙᴇʟᴜᴍ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.</b></blockquote>")
    except UserBannedInChannel:
        await mex.edit(f"<blockquote><b>{ggl} ᴀɴᴅᴀ ᴅɪʙᴀɴɴᴇᴅ ᴅɪ ᴄʜᴀɴɴᴇʟ/ɢʀᴜᴘ ɪɴɪ.</b></blockquote>")
    except Exception as e:
        await mex.edit(f"<blockquote><b>⚠️ ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("jvc")
@PY.TOP_CMD
@PY.GROUP
async def join_vc(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    
    mex = await message.reply(f"<blockquote><b>{prs} ᴘʀᴏᴄᴇssɪɴɢ...</b></blockquote>")
    try:
        # Menjalankan play kosong agar bisa join dan langsung mute
        await client.call_py.play(message.chat.id)
        await client.call_py.mute_stream(message.chat.id)
        await mex.edit(f"<blockquote><b>{brhsl} ʙᴇʀʜᴀsɪʟ ᴊᴏɪɴ ᴋᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.</b></blockquote>")        
    except ChatAdminRequired:
        await mex.edit(f"<blockquote><b>{ggl} ᴍᴀᴀꜰ, ᴀɴᴅᴀ ʙᴜᴛᴜʜ ɪᴢɪɴ ᴀᴅᴍɪɴ ᴜɴᴛᴜᴋ ᴊᴏɪɴ ᴠᴄ.</b></blockquote>")
    except UserBannedInChannel:
        await mex.edit(f"<blockquote><b>{ggl} ᴀɴᴅᴀ ᴅɪʙᴀɴɴᴇᴅ ᴅɪ ᴄʜᴀɴɴᴇʟ/ɢʀᴜᴘ ɪɴɪ.</b></blockquote>")
    except Exception as e:
        await mex.edit(f"<blockquote><b>⚠️ ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        