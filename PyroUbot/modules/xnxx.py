import requests
import os
from PyroUbot import *

__MODULE__ = "xɴxx"
__HELP__ = """
<blockquote><b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ xɴxx ⦫</b>

<b>⎆ ᴘᴇʀɪɴᴛᴀʜ :</b>
ᚗ <code>{0}xɴxx</code> [ᴋᴀᴛᴀ ᴋᴜɴᴄɪ]

<b>⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>
ᚗ ᴍᴇɴᴄᴀʀɪ ᴅᴀɴ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ᴅᴀʀɪ xɴxx.</blockquote>
"""

@PY.UBOT("xnxx")
async def random_bokep(client, message):
    try:
        query = message.text.split()[1:]
        if not query:
            return await message.reply("<blockquote><b><emoji id=5215204871422093648>❌</emoji> ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ: <code>.xɴxx</code> [ᴋᴀᴛᴀ ᴋᴜɴᴄɪ]</b></blockquote>")
        
        search_query = " ".join(query[:4])
        status_msg = await message.reply(f"<blockquote><b><emoji id=4967797089971995307>🔍</emoji> ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴜɴᴛᴜᴋ: <code>{search_query}</code>...</b></blockquote>")

        api_url = f"https://api.botcahx.eu.org/api/search/xnxx?query={search_query}&apikey=@iqbalnew77"
        
        response = requests.get(api_url)
        response.raise_for_status()
        api = response.json()

        results = api.get('result', [])
        if not results:
            return await status_msg.edit(f"<blockquote><b><emoji id=5215204871422093648>❌</emoji> ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ ʜᴀsɪʟ ᴜɴᴛᴜᴋ: <code>{search_query}</code></b></blockquote>")

        data = results[0]

        capt = (
            f"<blockquote><b>🎥 ʜᴀsɪʟ ᴘᴇɴᴄᴀʀɪᴀɴ: {search_query}</b>\n\n"
            f"  ◦ <b>ᴛɪᴛʟᴇ</b> : {data.get('title', 'ɴ/ᴀ')}\n"
            f"  ◦ <b>ᴠɪᴇᴡs</b> : {data.get('views', 'ɴ/ᴀ')}\n"
            f"  ◦ <b>ǫᴜᴀʟɪᴛʏ</b> : {data.get('quality', 'ɴ/ᴀ')}\n"
            f"  ◦ <b>ᴅᴜʀᴀᴛɪᴏɴ</b> : {data.get('duration', 'ɴ/ᴀ')}\n"
            f"  ◦ <b><a href='{data.get('link', 'ɴ/ᴀ')}'>🔗 ʟɪɴᴋ ᴠɪᴅᴇᴏ</a></b></blockquote>"
        )

        await status_msg.edit(f"<blockquote><b>📥 ᴍᴇɴɢᴜɴᴅᴜʜ ᴠɪᴅᴇᴏ:\n<code>{data.get('title', 'ɴ/ᴀ')}</code>...</b></blockquote>")

        dl_url = f"https://api.botcahx.eu.org/api/download/xnxxdl?url={data['link']}&apikey=@iqbalnew77"
        dl_response = requests.get(dl_url)
        dl_response.raise_for_status()
        dl_data = dl_response.json()
        video_url = dl_data.get('result', {}).get('url')

        if not video_url:
            return await status_msg.edit("<blockquote><b><emoji id=5215204871422093648>❌</emoji> ɢᴀɢᴀʟ ᴍᴇɢᴀᴍʙɪʟ ᴜʀʟ ᴠɪᴅᴇᴏ.</b></blockquote>")

        video_path = "video_xnxx.mp4"

        with requests.get(video_url, stream=True) as vid_res:
            vid_res.raise_for_status()
            with open(video_path, "wb") as f:
                for chunk in vid_res.iter_content(chunk_size=8192):
                    f.write(chunk)

        await status_msg.edit("<blockquote><b>📤 ᴍᴇɴɢᴜɴɢɢᴀʜ ᴠɪᴅᴇᴏ ᴋᴇ ᴛᴇʟᴇɢʀᴀᴍ...</b></blockquote>")
        
        await client.send_video(message.chat.id, video_path, caption=capt)
        
        if os.path.exists(video_path):
            os.remove(video_path)

        await status_msg.delete()

    except Exception as e:
        await message.reply(f"<blockquote><b><emoji id=5215204871422093648>❌</emoji> ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ:</b>\n<code>{str(e)}</code></blockquote>")
        
        
