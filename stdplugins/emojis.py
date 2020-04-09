"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""
from telethon import events
import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="spam (.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 16)
    input_str = event.pattern_match.group(1)
    if input_str == "plugin":
        await event.edit("@UserBotPlugin")
    elif input_str == "whatsapp":
        await event.edit("https://chat.whatsapp.com/K2QOz1RdpBO85AsGrkd6xL")
    elif input_str == "youtube":
        await event.edit(input_str)
        animation_chars = [
            "XxGamerQSDProXx ElectroFazYT",
            "XxGamerQSDProXx ElectroFazYT"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 2])
    elif input_str == "-_-":
        await event.edit(input_str)
        animation_chars = [
            "-__-",
            "-_-"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 2])
