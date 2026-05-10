import os
import json
import asyncio
import psutil
from datetime import datetime
from gc import get_objects
from time import time
from pyrogram.raw.functions import Ping
from PyroUbot import *

__MODULE__ = "ᴘɪɴɢ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘɪɴɢ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘɪɴɢ</code>
ᚗ <code>1ᴘɪɴɢ</code> [ᴜsᴇʀɴᴀᴍᴇ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴇᴄᴇᴋ ᴋᴇᴄᴇᴘᴀᴛᴀɴ ʀᴇsᴘᴏɴ ᴅᴀɴ sᴛᴀᴛᴜs ᴜsᴇʀʙᴏᴛ.</blockquote>
"""

@PY.UBOT("ping")
async def ping_handler(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    
    delta_ping = round((end - start).microseconds / 10000, 2)
    ping_res = str(delta_ping).replace('.', ',')
    
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    pantek = await STR.PONG(client)
    ngentod = await STR.OWNER(client)
    kontol = await STR.UBOT(client)
    
    is_prem = client.me.is_premium
    
    if is_prem:
        res = f"""
<blockquote>{pong} <b>{pantek} :</b> <code>{ping_res} ᴍs</code>
{tion} <b>{ngentod} :</b> <code>{client.me.mention}</code>
{yubot} <b>{kontol} :</b> <code>{bot.me.mention}</code></blockquote>
<blockquote><b>🚨 ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ 🚨</b></blockquote>"""
    else:
        res = f"""
<blockquote><b>{pantek} :</b> <code>{ping_res} ᴍs</code>
<b>{ngentod} :</b> <code>{client.me.mention}</code>
<b>{kontol} :</b> <code>{bot.me.mention}</code></blockquote>
<blockquote><b>🚨 ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ 🚨</b></blockquote>"""
    
    await message.reply(res)

@PY.INDRI("1ping")
async def indri_ping_handler(client, message):
    command = message.text.split()
    if len(command) < 2:
        return
    
    haku = command[1].replace("@", "")

    if client.me.username != haku:
        return
        
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    
    delta_ping = round((end - start).microseconds / 10000, 2)
    ping_res = str(delta_ping).replace('.', ',')
    
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    
    if client.me.is_premium:
        res = f"""
<blockquote>{pong} <b>ᴘᴏɴɢ :</b> <code>{ping_res} ᴍs</code>
{tion} <b>ᴏᴡɴᴇʀ :</b> {client.me.mention}
{yubot} <b>ᴜʙᴏᴛ :</b> {bot.me.mention}</blockquote>
<blockquote><b>🚨 ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ 🚨</b></blockquote>"""
    else:
        res = f"""
<blockquote><b>ᴘᴏɴɢ :</b> <code>{ping_res} ᴍs</code></blockquote>
<blockquote><b>ᴜʙᴏᴛ ɪǫʙᴀʟ ᴘʀᴇᴍɪᴜᴍ @ubotv2iqbal_bot</b></blockquote>"""
    
    await message.reply(res)
    