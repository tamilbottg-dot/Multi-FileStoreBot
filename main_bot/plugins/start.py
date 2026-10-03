"""Main controller start/menu handlers for Multi-FileStoreBot."""
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import ABOUT_MSG, OWNER_ID, MAX_BOTS_PER_USER
from database.main_db import MainDB

main_db = MainDB()
UPDATES_URL = "https://t.me/Toonworld4all_Tamil"
DEVELOPER_URL = "https://t.me/MrNarutotamil"


def get_main_menu():
    """Return the controller's main menu keyboard."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⚡️ ᴄʀᴇᴀᴛᴇ ʙᴏᴛ", callback_data="create_bot"),
         InlineKeyboardButton("📋 ᴍʏ ʙᴏᴛs", callback_data="my_bots")],
        [InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data="about")],
        [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs", url=UPDATES_URL),
         InlineKeyboardButton("👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=DEVELOPER_URL)],
    ])


def _welcome_text(user):
    name = user.first_name or "there"
    return (
        "<b>━━━━━━━━━━━━━━━━━━━━━\n"
        "🤖 𝗠𝗨𝗟𝗧𝗜-𝗙𝗜𝗟𝗘𝗦𝗧𝗢𝗥𝗘 𝗕𝗢𝗧\n"
        "━━━━━━━━━━━━━━━━━━━━━</b>\n\n"
        f"<blockquote>ʜᴇʟʟᴏ {name}!\n\n"
        "ᴄʀᴇᴀᴛᴇ ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ᴏᴡɴ ꜰɪʟᴇsᴛᴏʀᴇ ʙᴏᴛs ʜᴇʀᴇ.\n"
        f"ʏᴏᴜ ᴄᴀɴ ᴄʀᴇᴀᴛᴇ ᴜᴘ ᴛᴏ {MAX_BOTS_PER_USER} ʙᴏᴛs.</blockquote>"
    )


@Client.on_message(filters.private & filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply_text(_welcome_text(message.from_user), reply_markup=get_main_menu())


@Client.on_callback_query(filters.regex(r"^back_menu$"))
async def back_menu_callback(client: Client, query: CallbackQuery):
    from main_bot.plugins.create_bot import _creation_state
    _creation_state.pop(query.from_user.id, None)
    await query.message.edit_text(_welcome_text(query.from_user), reply_markup=get_main_menu())
    await query.answer()


@Client.on_callback_query(filters.regex(r"^about$"))
async def about_callback(client: Client, query: CallbackQuery):
    await query.message.edit_text(
        ABOUT_MSG,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs", url=UPDATES_URL),
             InlineKeyboardButton("👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=DEVELOPER_URL)],
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ ᴛᴏ ᴍᴇɴᴜ", callback_data="back_menu")],
        ]),
    )
    await query.answer()
