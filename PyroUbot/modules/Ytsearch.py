import os
import requests
from PyroUbot import *

# ᴍᴀsᴜᴋᴋᴀɴ ᴀᴘɪ ᴋᴇʏ ᴀɴᴅᴀ ᴅɪ sɪɴɪ
API_KEY = "@iqbalnew77"  # ɢᴀɴᴛɪ ᴅᴇɴɢᴀɴ ᴀᴘɪ ᴋᴇʏ ʏᴀɴɢ ʙᴇɴᴀʀ

__MODULE__ = "ʏᴛsᴇᴀʀᴄʜ"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʏᴛsᴇᴀʀᴄʜ ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}ʏᴛsᴇᴀʀᴄʜ</code> [ᴋᴀᴛᴀ ᴋᴜɴᴄɪ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴅɪ ʏᴏᴜᴛᴜʙᴇ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ.</blockquote>
"""

def fetch_youtube(api_url, query):
    """
    ꜰᴜɴɢsɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ᴅᴀʀɪ ᴀᴘɪ ʏᴏᴜᴛᴜʙᴇ
    """
    params = {"query": query, "apikey": API_KEY}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        # ᴍᴇᴍᴇʀɪᴋsᴀ ᴀᴘᴀᴋᴀʜ ʀᴇsᴘᴏɴs ʙᴇʀɪsɪ ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ
        data = response.json()
        if "result" in data:
            return data["result"]
        else:
            print("ᴛɪᴅᴀᴋ ᴀᴅᴀ ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ᴅᴀʟᴀᴍ ʀᴇsᴘᴏɴsᴇ:", data)
            return None
    except requests.exceptions.RequestException as e:
        print(f"ᴇʀʀᴏʀ ꜰᴇᴛᴄʜɪɴɢ ʏᴏᴜᴛᴜʙᴇ ʀᴇsᴜʟᴛs: {e}")
        return None

async def process_youtube_command(client, message, api_url, command_name):
    """
    ꜰᴜɴɢsɪ ᴜᴍᴜᴍ ᴜɴᴛᴜᴋ ᴍᴇɴᴀɴɢᴀɴɪ ᴘᴇʀɪɴᴛᴀʜ ᴘᴇɴᴄᴀʀɪᴀɴ ʏᴏᴜᴛᴜʙᴇ
    """
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text(f"<blockquote><b>**ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ:** <code>/{command_name}</code> [ᴋᴀᴛᴀ ᴋᴜɴᴄɪ]\n\nᴄᴏɴᴛᴏʜ: <code>/{command_name} ʟᴀɢᴜ ᴊᴀᴡᴀ</code></b></blockquote>")
        return

    query = args[1]
    status_msg = await message.reply_text("<blockquote><b>🔍 sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ...</b></blockquote>")

    results = fetch_youtube(api_url, query)
    if results:
        # ᴍᴇɴɢɪʀɪᴍᴋᴀɴ ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ sᴇʙᴀɢᴀɪ ᴅᴀꜰᴛᴀʀ
        response_text = (
            "<blockquote><b><emoji id=5841235769728962577>📹</emoji> ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ ʏᴏᴜᴛᴜʙᴇ</b></blockquote>\n\n"
        )
        for idx, result in enumerate(results[:5], start=1):  # ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ʜɪɴɢɢᴀ 5 ʜᴀsɪʟ sᴀᴊᴀ
            title = result.get("title", "ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴊᴜᴅᴜʟ")
            link = result.get("url", "ᴛɪᴅᴀᴋ ᴀᴅᴀ ʟɪɴᴋ")
            duration = result.get("duration", "ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴋᴛᴀʜᴜɪ")
            views = result.get("views", "ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴋᴛᴀʜᴜɪ")
            response_text += (
                f"<blockquote><b><emoji id=5841243255856960314>{idx}.</emoji> {title}</b>\n"
                f"<b>  ⏱️ ᴅᴜʀᴀsɪ:</b> {duration}\n"
                f"<b>  👁‍🗨 ᴠɪᴇᴡs:</b> {views}\n"
                f"<b>  🔗 ʟɪɴᴋ:</b> <a href='{link}'>ᴛᴏɴᴛᴏɴ ᴠɪᴅᴇᴏ</a></blockquote>\n"
            )
        await status_msg.edit(response_text, disable_web_page_preview=True)
    else:
        await status_msg.edit("<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ. ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ.</b></blockquote>")

# ʜᴀɴᴅʟᴇʀ ᴜɴᴛᴜᴋ ᴘᴇʀɪɴᴛᴀʜ ʏᴛsᴇᴀʀᴄʜ
@PY.UBOT("ytsearch")
async def youtube_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/search/yts"
    await process_youtube_command(client, message, api_url, "ʏᴛsᴇᴀʀᴄʜ")
    
