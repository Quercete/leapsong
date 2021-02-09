import asyncio
import re
import datetime

import discord

from src.smplemb import sample_embed
from src.utils.embedfactory import embed_factory

GPG_PREFIX_REGEX = re.compile(r"^!(gpg|pgp) ")


async def message_root(message: discord.Message):
    content = message.content
    is_gpg_command = re.match(GPG_PREFIX_REGEX, content)

    if is_gpg_command:
        command_body = re.sub(GPG_PREFIX_REGEX, "", content)
        if command_body.startswith("test"):
            if "already_registered" in command_body:
                embed = embed_factory(
                    user_display_name=message.author.display_name,
                    user_abatar_url=message.author.avatar_url,
                    user_id=message.author.id,
                    key_fingerprint="E27E 14ED 6771 02F5 051D 6E31 C046 9D56 0DE4 1848",
                    key_id="17CF 9C20 46CF 1B67",
                    valid_date=datetime.datetime.now()
                )
                await message.channel.send(embed=embed)
                return

            if "not_registered" in command_body:
                embed = embed_factory(
                    user_display_name=message.author.display_name,
                    user_abatar_url=message.author.avatar_url,
                    user_id=message.author.id
                )
                await message.channel.send(embed=embed)
                return
