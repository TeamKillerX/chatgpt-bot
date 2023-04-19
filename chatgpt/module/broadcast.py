# credits @xtsea

from pyrogram import Client as app
from pyrogram import *
from pyrogram.types import *
from chatgpt.database import cli
from config import ADMINS

collection = cli["chatgpt"]["welcome"]

@app.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast(client: Client, message: Message):
    user_db = await collection.find({})
    DEVS = [1191668125]
    text = message.text.split(" ", 1)[1] if len(message.command) > 1 else None
    if not text:
        await message.reply_text("please write an example <code>/broadcast test</code>")
        return
    done = 0
    for user in user_db:
        user_id = user.get("_id")
        if user_id in DEVS:
            continue
        try:
            await client.send_message(user_id, text)
            done += 1
        except Exception as e:
            await message.reply_text(f"Error : {e}")
            return
    await message.reply_text(f"Successfully sent to {done} users.")
