import asyncio
import speedtest
from pyrogram import filters
from PyroUbot import *

__MODULE__ = "sᴘᴇᴇᴅᴛᴇsᴛ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴘᴇᴇᴅᴛᴇsᴛ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}sᴘᴇᴇᴅᴛᴇsᴛ</code> | ᴍᴇɴɢᴜᴊɪ ᴋᴇᴄᴇᴘᴀᴛᴀɴ sᴇʀᴠᴇʀ ᴠᴘs.

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ :</b>
ᚗ ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ʜᴀsɪʟ ᴅᴀʟᴀᴍ ʙᴇɴᴛᴜᴋ ɢᴀᴍʙᴀʀ ɢʀᴀғɪᴋ.</blockquote>
"""

def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()
    st.download()
    st.upload()
    return st.results.dict()

@PY.UBOT("speedtest")
@PY.TOP_CMD
async def speedtest_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    ggl_emo = await EMO.GAGAL(client)
    brhsl_emo = await EMO.BERHASIL(client)
    
    Tm = await message.reply(f"<blockquote><b>{prs_emo} sᴇᴅᴀɴɢ ᴍᴇɴɢᴜᴊɪ ᴋᴇᴄᴇᴘᴀᴛᴀɴ ᴠᴘs...</b></blockquote>")
    
    try:
        # Menjalankan speedtest di thread terpisah agar tidak blocking
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, run_speedtest)
        
        link_grafik = data['share'] # Ini API bawaan speedtest buat gambar
        
        res = f"""
<blockquote><b>{brhsl_emo} sᴘᴇᴇᴅᴛᴇsᴛ sᴇʟᴇsᴀɪ</b>

<b>ᚗ ɪsᴘ :</b> <code>{data['client']['isp']}</code>
<b>ᚗ ᴘɪɴɢ :</b> <code>{data['ping']} ᴍs</code>
<b>ᚗ ᴅᴏᴡɴʟᴏᴀᴅ :</b> <code>{round(data['download'] / 10**6, 2)} ᴍʙᴘs</code>
<b>ᚗ ᴜᴘʟᴏᴀᴅ :</b> <code>{round(data['upload'] / 10**6, 2)} ᴍʙᴘs</code>

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ</blockquote>"""
        
        await client.send_photo(
            chat_id=message.chat.id,
            photo=link_grafik,
            caption=res,
            reply_to_message_id=message.id
        )
        await Tm.delete()
        
    except Exception as e:
        await Tm.edit(f"<blockquote><b>{ggl_emo} ᴇʀʀᴏʀ:</b> <code>{str(e)}</code></blockquote>")

