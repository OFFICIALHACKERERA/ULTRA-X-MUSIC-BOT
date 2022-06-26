""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)
from config import GROUP_SUPPORT, UPDATES_CHANNEL

def stream_markup(user_id):
  buttons = [
  
    [
      InlineKeyboardButton(text="•ɢʀᴏᴜᴘ•", url=f"https://t.me/HEPPYLIFI"),
      InlineKeyboardButton(text="•ᴏᴡɴᴇʀ•", url=f"https://t.me/OFFICIALHACKERERA"),
      InlineKeyboardButton(text="•ᴄʜᴀɴɴᴇʟ•", url=f"https://t.me/Broken_Heart_72"),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="⏹", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="⏸", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▶️", callback_data=f'cbresume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'cbunmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🗑 Close", callback_data='cls'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Close", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Go Back", callback_data="cbmenu"
      )
    ]
  ]
)
