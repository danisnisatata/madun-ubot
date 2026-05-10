import re
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PyroUbot import *

def detect_url_links(text):
    link_pattern = r"(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:[/?]\S+)?"
    return re.findall(link_pattern, text)

class BTN:
    
    def ALIVE(get_id):
        button = [
            [InlineKeyboardButton(text="𝗧𝗨𝗧𝗨𝗣", callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}")],
            [InlineKeyboardButton(text="𝗛𝗘𝗟𝗣", callback_data="help_back")]
        ]
        return button
        
    def PROMODEK(message):
        button = [
            [InlineKeyboardButton("𝗦𝗘𝗧𝗨𝗝𝗨 & 𝗟𝗔𝗡𝗝𝗨𝗧𝗞𝗔𝗡", callback_data="role_menu")],
        ]
        return button

    def BOT_HELP(message):
        button = [
            [InlineKeyboardButton("𝗥𝗘𝗦𝗧𝗔𝗥𝗧", callback_data="reboot")],
            [InlineKeyboardButton("𝗦𝗬𝗦𝗧𝗘𝗠", callback_data="system")],
            [InlineKeyboardButton("𝗨𝗕𝗢𝗧", callback_data="ubot")],
            [InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘", callback_data="update")],
        ]
        return button

    def START(message):
        UserId = message.from_user.id
        if UserId == 1850699314:
            button = [
                [InlineKeyboardButton("✅ 𝗕𝗨𝗔𝗧 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗚𝗥𝗔𝗧𝗜𝗦 ✅", callback_data="bahan")],
                [
                    InlineKeyboardButton("🔄 𝗥𝗘𝗦𝗧𝗔𝗥𝗧 𝗕𝗢𝗧", callback_data="cb_restart"),
                    InlineKeyboardButton("📥 𝗚𝗜𝗧𝗣𝗨𝗟𝗟", callback_data="cb_gitpull")
                ],
                [InlineKeyboardButton("📋 𝗟𝗜𝗦𝗧 𝗨𝗦𝗘𝗥𝗕𝗢𝗧", callback_data="cek_ubot")],
                [InlineKeyboardButton("📢 𝗥𝗢𝗢𝗠 𝗣𝗨𝗕𝗟𝗜𝗖", url="https://t.me/publicmadunn")],
                [InlineKeyboardButton("💬 𝗦𝗨𝗣𝗣𝗢𝗥𝗧", callback_data="support")]
            ]
        else:
            button = [
                [InlineKeyboardButton("✅ 𝗕𝗨𝗔𝗧 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗚𝗥𝗔𝗧𝗜𝗦 ✅", callback_data="bahan")],
                [InlineKeyboardButton("📢 𝗥𝗢𝗢𝗠 𝗣𝗨𝗕𝗟𝗜𝗖", url="https://t.me/publicmadunn")],
                [
                    InlineKeyboardButton("🚀 𝗕𝗨𝗔𝗧 𝗨𝗦𝗘𝗥𝗕𝗢𝗧", callback_data="buat_ubot"),
                    InlineKeyboardButton("❓ 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨", callback_data="help_back")
                ],
                [InlineKeyboardButton("💬 𝗦𝗨𝗣𝗣𝗢𝗥𝗧", callback_data="support")]
            ]
        return button

    def ADD_EXP(user_id):
        from pykeyboard import InlineKeyboard
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} 𝗕𝗨𝗟𝗔𝗡",
                    callback_data=f"success {user_id} member {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(
            InlineKeyboardButton(
                "📋 𝗗𝗔𝗣𝗔𝗧𝗞𝗔𝗡 𝗣𝗥𝗢𝗙𝗜𝗟", callback_data=f"profil {user_id}"
            )
        )
        buttons.row(
            InlineKeyboardButton(
                "❌ 𝗧𝗢𝗟𝗔𝗞 𝗣𝗘𝗠𝗕𝗔𝗬𝗔𝗥𝗔𝗡", callback_data=f"failed {user_id}"
            )
        )
        return buttons

    def EXP_UBOT():
        button = [
            [InlineKeyboardButton("✅ 𝗕𝗨𝗔𝗧 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗚𝗥𝗔𝗧𝗜𝗦", callback_data="bahan")],
        ]
        return button

    def UBOT(user_id, count):
        button = [
            [InlineKeyboardButton("🗑️ 𝗛𝗔𝗣𝗨𝗦 𝗗𝗔𝗥𝗜 𝗗𝗔𝗧𝗔𝗕𝗔𝗦𝗘", callback_data=f"del_ubot {int(user_id)}")],
            [InlineKeyboardButton("📅 𝗖𝗘𝗞 𝗠𝗔𝗦𝗔 𝗔𝗞𝗧𝗜𝗙", callback_data=f"cek_masa_aktif {int(user_id)}")],
            [
                InlineKeyboardButton("📨 𝗚𝗘𝗧 𝗢𝗧𝗣", callback_data=f"get_otp {int(count)}"),
                InlineKeyboardButton("📱 𝗚𝗘𝗧 𝗣𝗛𝗢𝗡𝗘", callback_data=f"get_phone {int(count)}")
            ],
            [
                InlineKeyboardButton("⬅️ 𝗦𝗘𝗕𝗘𝗟𝗨𝗠𝗡𝗬𝗔", callback_data=f"p_ub {int(count)}"),
                InlineKeyboardButton("𝗦𝗘𝗟𝗔𝗡𝗝𝗨𝗧𝗡𝗬𝗔 ➡️", callback_data=f"n_ub {int(count)}")
            ],
            [InlineKeyboardButton("🔙 𝗞𝗘𝗠𝗕𝗔𝗟𝗜", callback_data="bahan")]
        ]
        return button
    
    def DEAK(user_id, count):
        button = [
            [
                InlineKeyboardButton("🔙 𝗞𝗘𝗠𝗕𝗔𝗟𝗜", callback_data=f"p_ub {int(count)}"),
                InlineKeyboardButton("✅ 𝗦𝗘𝗧𝗨𝗝𝗨𝗜", callback_data=f"deak_akun {int(count)}"),
            ],
        ]
        return button
