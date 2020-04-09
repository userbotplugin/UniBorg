from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="user"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("💥Entra in @UserBotPlugin💥!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("💥Entra in @UserBotPlugin💥!\n{}".format(ms))
