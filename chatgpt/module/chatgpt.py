# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

import requests
import os
import json
import random
import asyncio
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren 
from pyrogram.errors import MessageNotModified
from chatgpt.module.what import *
from config import OPENAI_API 

@ren.on_message(filters.command("ask") & filters.private | filters.group)
async def chatgpt(c: Client, m: Message):
    randydev = (
        m.text.split(None, 1)[1]
        if len(
            m.command,
        )
        != 1
        else None
    )
    if not randydev:
       await m.reply(f"use command <code>/{m.command[0]} [question]</code> to ask questions using the API.")
       return
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "prompt": randydev,
        "model": "text-davinci-003",
        "temperature": 0.5,
        "max_tokens": 1024,
        "n": 1,
        "stop": None,
        "top_p": 0.3,
        "frequency_penalty": 0.5,
    }
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        await asyncio.sleep(5)
        await c.send_message(m.chat.id, response["choices"][0]["text"], reply_to_message_id=m.id)
    except Exception:
        await c.send_message(m.chat.id, "Yahh, sorry i can't get your answer.", reply_to_message_id=m.id)
