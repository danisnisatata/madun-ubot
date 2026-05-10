import asyncio
import os
import sys
import signal
import tornado.ioloop
import tornado.platform.asyncio
from pyrogram import Client, filters
from PyroUbot import *

# --- HANDLER RESTART (NAMA & ID SESUAI PENGIRIM) ---
@bot.on_message(filters.command("restart"))
async def restart_bot_utama(client, message):
    # Ambil data orang yang ngetik perintah
    pengirim_name = message.from_user.first_name
    pengirim_id = message.from_user.id

    # Pesan awal font Smallcaps
    status = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>")
    
    # Jeda biar efek edit kelihatan
    await asyncio.sleep(2)
    
    # Edit pesan: Nama & ID otomatis jadi milik si pengirim
    await status.edit(
        f"<b>ʀᴇsᴛᴀʀᴛ ʙᴇʀʜᴀsɪʟ ᴅɪʟᴀᴋᴜᴋᴀɴ !</b>\n\n"
        f"<b>ɴᴀᴍᴇ:</b> {pengirim_name} | <code>{pengirim_id}</code>"
    )
    
    # Eksekusi restart sistem
    os.execl(sys.executable, sys.executable, "-m", "PyroUbot")

async def shutdown(signal, loop):
    print(f"Received exit signal {signal.name}...")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    print("Cancelling outstanding tasks")
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()

# --- FUNGSI NOTIFIKASI STARTUP ---
async def send_log_startup():
    await asyncio.sleep(5) 
    ID_LOG_CHANNEL = -1007194583122 
    
    if ubot._ubot:
        akun_utama = ubot._ubot[0]
        try:
            text_start = (
                f"<b>ᴍʏ ᴜʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ</b>\n"
                f"<b>❑ ᴜsᴇʀʙᴏᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>\n"
                f"<b>├ ᴀᴋᴜɴ: {akun_utama.me.first_name}</b>\n"
                f"<b>└ ɪᴅ: <code>{akun_utama.me.id}</code></b>"
            )
            await bot.send_message(ID_LOG_CHANNEL, text_start)
        except Exception as e:
            print(f"Gagal kirim log ke CH: {e}")

async def main():
    await bot.start()
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await asyncio.wait_for(ubot_.start(), timeout=10)
        except asyncio.TimeoutError:
            await remove_ubot(int(_ubot["name"]))
            print(f"[ɪɴғᴏ]: {int(_ubot['name'])} ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇʀᴇsᴘᴏɴ")
        except Exception:
            await remove_ubot(int(_ubot["name"]))
            print(f"[ɪɴғᴏ]: {int(_ubot['name'])} ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs")
    
    await bash("rm -rf *session*")
    
    await asyncio.gather(loadPlugins(), installPeer())
    
    asyncio.create_task(send_log_startup())
    
    stop_event = asyncio.Event()
    loop = asyncio.get_running_loop()
    for s in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(
            s, lambda: asyncio.create_task(shutdown(s, loop))
        )

    try:
        await stop_event.wait()
    except asyncio.CancelledError:
        pass
    finally:
        await bot.stop()

if __name__ == "__main__":
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    loop = tornado.ioloop.IOLoop.current().asyncio_loop
    loop.run_until_complete(main())
    