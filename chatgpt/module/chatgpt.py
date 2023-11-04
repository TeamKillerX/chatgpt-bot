# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

import asyncio
from pyrogram.types import Message
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren
import database as db

from RyuzakiLib.hackertools.openai import OpenAiToken

CMD_HANDLER = ["!", "/"]

cmd = CMD_HANDLER

@ren.on_message(filters.command("addkey"))
async def update_db_key(client: Client, message: Message):
    user_id = message.from_user.id
    text = message.text.split(" ", 1)[1] if len(message.command) > 1 else None
    if not text:
        await message.reply_text("Use Command /addkey apikey")
        return
    db.add_openai_api_key(user_id, text)
    await message.reply_text(f"Successfully added api key: {text}")

@ren.on_message(filters.command(["ai", "ask"], cmd) & filters.private | filters.group)
async def chatgpt(c: Client, m: Message):
    randydev = m.text.split(" ", 1)[1] if len(m.command) > 1 else None
    if not randydev:
       await m.reply(f"use command <code>/{m.command[0]} [question]</code> to ask questions using the API.")
       return
    try:
        user = db.get_openai_api_key(m.from_user.id)
        if user:
            openai_message = OpenAiToken(user)
            output_text = openai_message.message_output(randydev)
            await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
            await asyncio.sleep(2)
            await c.send_message(
                m.chat.id,
                output_text,
                reply_to_message_id=m.id
            )
        else:
            await c.send_message(m.chat.id, "Not Found User")
    except Exception:
        await c.send_message(m.chat.id, "Yahh, sorry i can't get your answer.", reply_to_message_id=m.id)

@ren.on_message(filters.command(["dalle"], cmd) & filters.private | filters.group)
async def dalle(c: Client, m: Message):
    randydev = m.text.split(" ", 1)[1] if len(m.command) > 1 else None
    if not randydev:
       await m.reply(f"use command <code>/{m.command[0]} [question]</code> to dall e image generator using the API.")
       return
    try:
        user = db.get_openai_api_key(m.from_user.id)
        if user:
            openai_message = OpenAiToken(user)
            output_photo = openai_message.photo_output(randydev)
            await c.send_chat_action(m.chat.id, enums.ChatAction.PHOTO)
            await asyncio.sleep(2)
            await c.send_photo(
                m.chat.id,
                output_photo,
                reply_to_message_id=m.id
            )
        else:
            await client.send_message(m.chat.id, "Not found user")
    except Exception:
        await c.send_message(m.chat.id, "Yahh, sorry i can't get your answer.", reply_to_message_id=m.id)
