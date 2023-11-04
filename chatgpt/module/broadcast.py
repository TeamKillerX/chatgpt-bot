from pyrogram.types import Message
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren
from config import ADMINS
import database as db

@ren.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast_user(client: Client, message: Message):
    text = message.text.split(" ", 1)[1] if len(message.command) > 1 else None
    if not text:
        await message.reply_text("Use Command /broadcast text")
        return
    blacklist = db.broadcast_only_bots()
    if blacklist:
        if message.from_user.id not in blacklist:
            await client.send_message(message.from_user.id, text=text)
        else:
            await message.reply_text("You are not allowed to use the broadcast feature.")
    else:
        await client.send_message(message.chat.id, "Missing Data")
