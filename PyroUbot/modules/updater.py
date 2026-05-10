import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from PyroUbot.config import OWNER_ID
import psutil
from PyroUbot import *


async def ngentod(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    
    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ᴘᴇᴍʙᴀʜᴀʀᴜᴀɴ...</b></blockquote>")
    
    try:
        out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
        if "Already up to date." in str(out):
            return await status_msg.edit(f"<blockquote><b>{brhsl} sʏsᴛᴇᴍ sᴜᴅᴀʜ ʙᴇʀᴀᴅᴀ ᴅɪ ᴠᴇʀsɪ ᴛᴇʀʙᴀʀᴜ.</b></blockquote>")
        
        result = f"<blockquote><b>✅ ʙᴇʀʜᴀsɪʟ ᴅɪᴘᴇʀʙᴀʜᴀʀᴜɪ!</b>\n\n<code>{out}</code></blockquote>"
        
        if len(result) > 4096:
            # Jika output terlalu panjang, kirim sebagai file atau potong
            await status_msg.edit(f"<blockquote><b>✅ ʙᴇʀʜᴀsɪʟ ᴅɪᴘᴇʀʙᴀʜᴀʀᴜɪ!</b>\n\n<i>ᴏᴜᴛᴘᴜᴛ ᴛᴇʀʟᴀʟᴜ ᴘᴀɴᴊᴀɴɢ, ᴍᴇʟᴀᴋᴜᴋᴀɴ ʀᴇsᴛᴀʀᴛ...</i></blockquote>")
        else:
            await status_msg.edit(result)
            
        # Proses Restart
        os.execl(sys.executable, sys.executable, "-m", "PyroUbot")
        
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")

@PY.BOT("update")
@PY.OWNER
async def _(c, m):
    await ngentod(c, m)


@PY.UBOT("update")
@PY.OWNER
async def _(c, m):
    await ngentod(c, m)
    