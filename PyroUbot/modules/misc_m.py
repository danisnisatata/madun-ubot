import asyncio
import os
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from PyroUbot import *

__MODULE__ = "ᴍɪsᴄ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍɪsᴄ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʟɪᴍɪᴛ</code>
⊷ ᴄᴇᴋ sᴛᴀᴛᴜs ʟɪᴍɪᴛ ᴀᴋᴜɴ
ᚗ <code>{0}ᴄᴀʀʙᴏɴ</code>
⊷ ᴍᴇʀᴜʙᴀʜ ᴛᴇᴋs ᴊᴀᴅɪ ɢᴀᴍʙᴀʀ ᴋᴏᴅᴇ
ᚗ <code>{0}ǫʀɢᴇɴ</code>
⊷ ᴍᴇʀᴜʙᴀʜ ᴛᴇᴋs ᴊᴀᴅɪ ǫʀᴄᴏᴅᴇ
ᚗ <code>{0}ǫʀʀᴇᴀᴅ</code>
⊷ ᴍᴇᴍʙᴀᴄᴀ ᴅᴀᴛᴀ ᴅᴀʀɪ ǫʀᴄᴏᴅᴇ
ᚗ <code>{0}ꜰᴏɴᴛ</code>
⊷ ᴍᴇʀᴜʙᴀʜ ɢᴀʏᴀ ᴛᴇᴋs ᴠɪᴀ ɪɴʟɪɴᴇ</blockquote>
"""

@PY.UBOT("limit")
@PY.TOP_CMD
async def limit_handler(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴄʜᴇᴄᴋ ʟɪᴍɪᴛ...</b></blockquote>")
    
    response = await client.invoke(
        StartBot(bot=bot_info, peer=bot_info, random_id=client.rnd_id(), start_param="start")
    )
    await asyncio.sleep(1)
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1)
    
    is_prem = "ᴛʀᴜᴇ" if client.me.is_premium else "ꜰᴀʟsᴇ (ʙᴇʟɪ ᴘʀᴇᴍ ᴅᴜʟᴜ)"
    limit_status = "ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ᴅɪʙᴀᴛᴀsɪ" if len(status.text) <= 100 else "ᴀᴋᴜɴ ᴀɴᴅᴀ ʙᴇʀᴍᴀsᴀʟᴀʜ / ʟɪᴍɪᴛ"

    res = f"""
<blockquote><b>{pong} sᴛᴀᴛᴜs ᴘʀᴇᴍɪᴜᴍ :</b> <code>{is_prem}</code>
<b>{tion} ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ :</b> <code>{limit_status}</code>
<b>{yubot} ᴜʙᴏᴛ :</b> {bot.me.mention}</blockquote>
<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>"""
    
    await status_msg.edit(res)
    await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))

@PY.UBOT("carbon")
@PY.TOP_CMD
async def carbon_handler(client, message):
    prs = await EMO.PROSES(client)
    args = get_arg(message) or (message.reply_to_message.text if message.reply_to_message else None)
    if not args:
        return await message.reply("<blockquote><b>ᚗ ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴛᴇᴋs ᴀᴛᴀᴜ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇsᴀɴ!</b></blockquote>")

    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴄᴀʀʙᴏɴ...</b></blockquote>")
    
    try:
        # Menggunakan API Carbonara
        url = "https://carbonara.solopov.dev/api/cook"
        resp = requests.post(url, json={"code": args})
        image = BytesIO(resp.content)
        image.name = "carbon.png"
        
        await client.send_photo(message.chat.id, image, caption=f"<blockquote><b>ᚗ ᴄᴀʀʙᴏɴɪᴢᴇᴅ ʙʏ :</b> {client.me.mention}</blockquote>")
        await status_msg.delete()
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("qrgen")
@PY.TOP_CMD
async def qrgen_handler(client, message):
    prs = await EMO.PROSES(client)
    args = get_arg(message) or (message.reply_to_message.text if message.reply_to_message else None)
    if not args:
        return await message.reply("<blockquote><b>ᚗ ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴛᴇᴋs ᴀᴛᴀᴜ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇsᴀɴ!</b></blockquote>")

    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍʙᴜᴀᴛ ǫʀᴄᴏᴅᴇ...</b></blockquote>")
    try:
        url = f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={args}"
        await client.send_photo(message.chat.id, url, caption=f"<blockquote><b>ᚗ ǫʀɢᴇɴ ʙʏ :</b> {client.me.mention}</blockquote>")
        await status_msg.delete()
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>⚠️ ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

@PY.UBOT("qrread")
@PY.TOP_CMD
async def qrread_handler(client, message):
    prs = await EMO.PROSES(client)
    replied = message.reply_to_message
    if not (replied and replied.media):
        return await message.reply("<blockquote><b>ᚗ ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ǫʀᴄᴏᴅᴇ (ɢᴀᴍʙᴀʀ)!</b></blockquote>")

    status_msg = await message.reply(f"<blockquote><b>{prs} sᴇᴅᴀɴɢ ᴍᴇᴍʙᴀᴄᴀ ǫʀᴄᴏᴅᴇ...</b></blockquote>")
    down_load = await client.download_media(message=replied)
    
    try:
        files = {'f': open(down_load, 'rb')}
        resp = requests.post("https://zxing.org/w/decode", files=files)
        soup = BeautifulSoup(resp.text, "html.parser")
        qr_contents = soup.find_all("pre")[0].text
        await status_msg.edit(f"<blockquote><b>ᚗ ᴅᴀᴛᴀ ǫʀᴄᴏᴅᴇ :</b>\n<code>{qr_contents}</code></blockquote>")
    except:
        await status_msg.edit("<blockquote><b>ᚗ ɢᴀɢᴀʟ ᴍᴇᴍʙᴀᴄᴀ ǫʀᴄᴏᴅᴇ ᴀᴛᴀᴜ ᴅᴀᴛᴀ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ.</b></blockquote>")
    
    if os.path.exists(down_load):
        os.remove(down_load)

@PY.UBOT("font")
@PY.TOP_CMD
async def font_handler(client, message):
    args = get_arg(message) or (message.reply_to_message.text if message.reply_to_message else None)
    if not args:
        return await message.reply("<blockquote><b>ᚗ ᴍᴏʜᴏɴ ʀᴇᴘʟʏ ᴋᴇ ᴛᴇᴋs ᴀᴛᴀᴜ ᴍᴀsᴜᴋᴋᴀɴ ᴘᴇsᴀɴ!</b></blockquote>")
    
    try:
        # Memanggil inline bot untuk pemilihan font
        x = await client.get_inline_bot_results(bot.me.username, f"get_font {id(message)}")
        await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as e:
        await message.reply(f"<blockquote><b>⚠️ ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")
        