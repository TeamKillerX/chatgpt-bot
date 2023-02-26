# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

import logging
from typing import *
from pyrogram import Client
from pyrogram import *
from pyrogram.types import *
from config import API_ID, API_HASH, BOT_TOKEN


logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    plugins = dict(root="chatgpt")

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins,
    workers=300,
)

app.run()
idle()
