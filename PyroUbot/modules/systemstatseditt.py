import platform
import sys
from datetime import datetime
import psutil
from asyncio import create_subprocess_exec as asyncrunapp
from pyrogram import filters, Client
from pyrogram import __version__
from pyrogram.types import Message
from PyroUbot import *

__MODULE__ = "sʏsᴛᴇᴍ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sʏsᴛᴇᴍ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴘᴄ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟɪʜᴀᴛ sᴛᴀᴛɪsᴛɪᴋ ᴅᴀɴ ɪɴꜰᴏʀᴍᴀsɪ ᴅᴇᴛᴀɪʟ sʏsᴛᴇᴍ sᴇʀᴠᴇʀ.</blockquote>
"""

async def get_readable_time(seconds: int) -> str: 
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["ᴅᴛᴋ", "ᴍɴᴛ", "ᴊᴀᴍ", "ʜᴀʀɪ"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time

def get_size(bytes, suffix="ʙ"):
    factor = 1024
    for unit in ["", "ᴋ", "ᴍ", "ɢ", "ᴛ", "ᴘ"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

@PY.UBOT("spc")
@PY.TOP_CMD
async def psu(client: Client, message: Message):
    uname = platform.uname()
    
    # System Info
    softw = f"<blockquote><b>ɪɴꜰᴏʀᴍᴀsɪ sʏsᴛᴇᴍ</b>\n"
    softw += f"ᚗ sʏsᴛᴇᴍ : <code>{uname.system}</code>\n"
    softw += f"ᚗ ʀɪʟɪs : <code>{uname.release}</code>\n"
    softw += f"ᚗ ᴠᴇʀsɪ : <code>{uname.version[:20]}...</code>\n"
    softw += f"ᚗ ᴍᴇsɪɴ : <code>{uname.machine}</code>\n"
    
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"ᚗ ᴡᴀᴋᴛᴜ ʜɪᴅᴜᴘ : <code>{bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}</code></blockquote>\n"

    # CPU Info
    cpuu = f"<blockquote><b>ɪɴꜰᴏʀᴍᴀsɪ ᴄᴘᴜ</b>\n"
    cpuu += f"ᚗ ᴘʜʏsɪᴄᴀʟ ᴄᴏʀᴇs : <code>{psutil.cpu_count(logical=False)}</code>\n"
    cpuu += f"ᚗ ᴛᴏᴛᴀʟ ᴄᴏʀᴇs : <code>{psutil.cpu_count(logical=True)}</code>\n"
    cpufreq = psutil.cpu_freq()
    cpuu += f"ᚗ ᴄᴜʀʀᴇɴᴛ ꜰʀᴇǫ : <code>{cpufreq.current:.2f}ᴍʜᴢ</code>\n"
    cpuu += f"ᚗ sᴇᴍᴜᴀ ᴄᴏʀᴇ : <code>{psutil.cpu_percent()}%</code></blockquote>\n"

    # Memory Usage
    svmem = psutil.virtual_memory()
    memm = f"<blockquote><b>ᴍᴇᴍᴏʀɪ ᴅɪɢᴜɴᴀᴋᴀɴ</b>\n"
    memm += f"ᚗ ᴛᴏᴛᴀʟ : <code>{get_size(svmem.total)}</code>\n"
    memm += f"ᚗ ᴜsᴇᴅ : <code>{get_size(svmem.used)}</code> (<code>{svmem.percent}%</code>)</blockquote>\n"

    # Bandwidth Usage
    bw = f"<blockquote><b>ʙᴀɴᴅᴡɪᴅᴛʜ ᴅɪɢᴜɴᴀᴋᴀɴ</b>\n"
    bw += f"ᚗ ᴜɴɢɢᴀʜ : <code>{get_size(psutil.net_io_counters().bytes_sent)}</code>\n"
    bw += f"ᚗ ᴜɴᴅᴜʜ : <code>{get_size(psutil.net_io_counters().bytes_recv)}</code></blockquote>\n"

    # Footer
    footer = f"<blockquote><b>ɪɴꜰᴏʀᴍᴀsɪ ᴍᴇsɪɴ</b>\n"
    footer += f"ᚗ ᴘʏᴛʜᴏɴ : <code>{sys.version.split()[0]}</code>\n"
    footer += f"ᚗ ᴘʏʀᴏɢʀᴀᴍ : <code>{__version__}</code>\n\n"
    footer += f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ {client.me.mention}</b></blockquote>"

    await message.reply(softw + cpuu + memm + bw + footer)
    