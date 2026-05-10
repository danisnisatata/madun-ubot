import aiohttp
from PyroUbot import *

__MODULE__ = "ɢᴏᴏɢʟᴇ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴏᴏɢʟᴇ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ɢᴏᴏɢʟᴇ</code> [ǫᴜᴇʀʏ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇɴᴇʟᴜsᴜʀᴀɴ ᴄᴇᴘᴀᴛ ᴅɪ ᴍᴇsɪɴ ᴘᴇɴᴄᴀʀɪ ɢᴏᴏɢʟᴇ.</blockquote>
"""

@PY.UBOT("gg|google|googlesearch")
@PY.TOP_CMD
async def google_search_handler(client, message):
    prs_emo = await EMO.PROSES(client)
    brhsl_emo = await EMO.BERHASIL(client)
    ggl_emo = await EMO.GAGAL(client)
    
    args = get_arg(message)
    if not args:
        return await message.reply_text(
            f"<blockquote><b>{ggl_emo} ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ!</b>\nᚗ ᴄᴏɴᴛᴏʜ: <code>.ɢᴏᴏɢʟᴇ ᴀᴘᴀ ɪᴛᴜ ᴜʙᴏᴛ?</code></blockquote>"
        )

    status_msg = await message.reply_text(f"<blockquote><b>{prs_emo} ᴍᴇɴᴇʟᴜsᴜʀɪ ɢᴏᴏɢʟᴇ...</b></blockquote>")
    
    api_url = f"https://aemt.uk.to/googlesearch?query={args}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, timeout=20) as response:
                if response.status == 200:
                    data = await response.json()
                    results = data.get("result", [])
                    
                    if not results:
                        return await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ʜᴀsɪʟ ᴜɴᴛᴜᴋ ǫᴜᴇʀʏ ᴛᴇʀsᴇʙᴜᴛ.</b></blockquote>")
                    
                    res_text = f"<blockquote><b>🔍 ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ɢᴏᴏɢʟᴇ</b>\n\n"
                    
                    # Ambil maksimal 5 hasil agar tidak terkena limit karakter
                    for result in results[:5]:
                        title = result.get("title", "ɴᴏ ᴛɪᴛʟᴇ")
                        link = result.get("link", "#")
                        desc = result.get("description", "ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴇsᴋʀɪᴘsɪ.")
                        
                        res_text += (
                            f"<b>ᚗ {title}</b>\n"
                            f"<b>⊷ ʟɪɴᴋ :</b> <a href='{link}'>ᴋʟɪᴋ ᴅɪ sɪɴɪ</a>\n"
                            f"<i>{desc}</i>\n\n"
                        )
                    
                    res_text += f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ :</b> ɪǫʙᴀʟ ᴜʙᴏᴛ</blockquote>"
                    
                    await status_msg.edit(res_text, disable_web_page_preview=True)
                else:
                    await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴇʀʀᴏʀ: ɢᴀɢᴀʟ ᴍᴇɴɢʜᴜʙᴜɴɢɪ sᴇʀᴠᴇʀ ᴀᴘɪ.</b></blockquote>")
                    
    except Exception as e:
        await status_msg.edit(f"<blockquote><b>{ggl_emo} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        