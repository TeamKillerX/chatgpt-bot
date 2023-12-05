# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from pyrogram import Client as ren
from pyrogram import *
from pyrogram.types import *
import database as db

@ren.on_message(filters.command("start") & filters.private)
async def start_welcome(client: Client, message: Message):
    MESSAGE = f"""
Hey there {message.from_user.mention}

• Welcome to my bot! Send me a message and I will use the Assistant Bot to generate a response.

- Command: /ai question 
- Command: /ai2 question
- Command: /bingai question
- Command: /jokeai question
- Command: /dalle image generator
- Command: /addkey setting api key

• Developer : t.me/xtdevs
"""
    db.start_bot(user_id)
    await client.send_message(message.chat.id, MESSAGE, reply_to_message_id=message.id, disable_web_page_preview=True)
