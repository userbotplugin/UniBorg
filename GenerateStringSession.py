#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""METTI API E HASH BY 💥XxGamerYT😈 info:+393791185645 telegram:@DIAVOLOGAMER""")
APP_ID = int(input("🌀Metti APP ID🌀: "))
API_HASH = input("⚡Metti API HASH⚡: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
