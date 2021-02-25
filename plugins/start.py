from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from vars import var


START_MSG = """
Hi, I am **Anonymous Messages Sender BOT.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!

You Can too Clone me :-
https://github.com/hackelite01/AnonymousMessagesSender
"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("鉂わ笍 Support Group 鉂わ笍",
                          url="t.me/hackelite01")],
    [InlineKeyboardButton("馃鈥嶐煉� Dev 馃鈥嶐煉�",
                          url="t.me/mayank1rajput")]])


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(START,
                             reply_markup=REPLY_MARKUP)
