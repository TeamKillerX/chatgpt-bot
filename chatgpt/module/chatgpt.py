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
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren 
from pyrogram.errors import MessageNotModified
from pykillerx.helper.what import *
from config import OPENAI_API 

@ren.on_message(filters.command("ask") & filters.group)
async def chatgpt(c: Client, m: Message):
    if len(m.command) == 1:
        return await m.reply(f"use command <code>.{m.command[0]} [question]</code> to ask questions using the API.")
    randydev = m.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": randydev,
        "max_tokens": 200,
        "temperature": 0,
    }
    ran = await m.reply("Wait a moment looking for your answer..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await ran.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await ran.edit("Yahh, sorry i can't get your answer.")
