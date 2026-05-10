import asyncio
from datetime import datetime
from time import time
from pyrogram.raw.functions import Ping
from PyroUbot import *

__MODULE__ = "ᴘɪɴɢ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘɪɴɢ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ᴘɪɴɢ</code> | <code>ᴘɪɴɢ1</code>
ᚗ <code>{0}ᴘɪɴɢ2</code> | <code>ᴘ</code>

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴɢᴇᴄᴇᴋ ᴋᴇᴄᴇᴘᴀᴛᴀɴ ʀᴇsᴘᴏɴ ʙᴏᴛ ᴅᴀɴ ᴡᴀᴋᴛᴜ ᴀᴋᴛɪꜰ sᴇʀᴠᴇʀ.</blockquote>
"""

async def get_ping_stats(client):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = round((end - start).microseconds / 10000, 2)
    uptime = await get_time((time() - start_time))
    return str(delta_ping).replace('.', ','), uptime

@PY.UBOT("ping")
async def ping_default(client, message):
    ping_res, uptime = await get_ping_stats(client)
    pong = await EMO.PING(client)
    ngentod = await STR.OWNER(client)
    kontol = await STR.UBOT(client)
    
    res = f"""
<blockquote>{pong} <b>{await STR.PONG(client)}</b> : <code>{ping_res} ᴍs</code>
<b>ᚗ {ngentod} :</b> <code>{client.me.mention}</code>
<b>ᚗ {kontol} :</b> <code>{bot.me.mention}</code></blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>"""
    await message.reply(res)

@PY.UBOT("ping1")
async def ping_v1(client, message):
    xx = await message.edit("𖣐")
    for i in range(2, 6):
        await asyncio.sleep(0.2)
        await xx.edit("𖣐" * i)
    await xx.edit("⚡")
    
    ping_res, uptime = await get_ping_stats(client)
    res = f"""
<blockquote>⎆ <emoji id=5260547274957672345>🎲</emoji> <b>ᴘɪɴɢ :</b> <code>{ping_res} ᴍs</code>
⎆ <emoji id=5235948055928262102>⭐</emoji> <b>ᴜᴘᴛɪᴍᴇ :</b> <code>{uptime}</code>
⎆ <emoji id=5204015897500469606>😢</emoji> <b>ᴋɪɴɢ :</b> <code>{client.me.mention}</code>
⎆ <emoji id=5194979342144260681>😂</emoji> <b>ᴡᴀʀʀɪᴏʀ :</b> <code>{bot.me.mention}</code></blockquote>
<blockquote><b><emoji id=6142927453854632687>🚬</emoji> ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ <emoji id=6142927453854632687>🚬</emoji></b></blockquote>"""
    await xx.edit(res)

@PY.UBOT("ping2")
async def ping_v2(client, message):
    xx = await message.edit("★ ᴘɪɴɢ ★")
    await asyncio.sleep(0.3)
    await xx.edit("✦҈͜͡➳ ᴘᴏɴɢ! 🌩")
    
    ping_res, uptime = await get_ping_stats(client)
    res = f"""
<blockquote><emoji id=5897929355216034070>🤩</emoji> ❃ <b>ᴘɪɴɢ !!</b>
<code>{ping_res} ᴍs</code>
<emoji id=5900041834880571364>😈</emoji> ❃ <b>ᴜᴘᴛɪᴍᴇ -</b>
<code>{uptime}</code>
<emoji id=5897741587835786345>🔥</emoji> <b>✦҈͜͡➳ ᴍᴀsᴛᴇʀ :</b>
<code>{client.me.mention}</code>
<emoji id=5900145373657176313>😂</emoji> <b>✦҈͜͡➳ ʙᴏᴛ :</b>
<code>{bot.me.mention}</code></blockquote>
<blockquote><b><emoji id=6142927453854632687>🚬</emoji> ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ <emoji id=6142927453854632687>🚬</emoji></b></blockquote>"""
    await xx.edit(res)

@PY.UBOT("p")
async def ping_short(client, message):
    await message.edit("■■■■■ <emoji id=6332421827565982132>😎</emoji>")
    await asyncio.sleep(0.3)
    
    ping_res, uptime = await get_ping_stats(client)
    res = f"""
<blockquote>⎆ <emoji id=6332421827565982132>😎</emoji> <b>ᴘɪɴɢ :</b> <code>{ping_res} ᴍs</code>
⎆ <emoji id=5080277662069425163>😎</emoji> <b>ᴜᴘᴛɪᴍᴇ :</b> <code>{uptime}</code>
⎆ <emoji id=5080240441882838117>😎</emoji> <b>ᴋɪɴɢ :</b> <code>{client.me.mention}</code>
⎆ <emoji id=5071138963800982678>😎</emoji> <b>ᴡᴀʀʀɪᴏʀ :</b> <code>{bot.me.mention}</code></blockquote>
<blockquote><b><emoji id=5400297831367979161>🗡</emoji> ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ <emoji id=5400297831367979161>🗡</emoji></b></blockquote>"""
    await message.edit(res)
    