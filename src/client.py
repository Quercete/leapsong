import asyncio
import os
import re
from typing import Union

import discord

from src.smplemb import sample_embed

TOKEN = os.getenv("TOKEN")
TEST_TEXT_CH_ID = 711127633810817026
GPG_PREFIX_REGEX = re.compile(r"^!(gpg|pgp) ")


class MainClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.TEST_TEXT_CH: Union[None, discord.TextChannel] = None

    async def on_ready(self):
        self.TEST_TEXT_CH = self.get_channel(TEST_TEXT_CH_ID)

    def run(self):
        super().run(TOKEN)

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        # TODO:ここから先をon_messageとかに渡す
        content = message.content
        is_gpg_command = re.match(GPG_PREFIX_REGEX, content)

        if is_gpg_command:
            command_body = re.sub(GPG_PREFIX_REGEX, "", content)
            if command_body.startswith("test"):
                await self.TEST_TEXT_CH.send(embed=sample_embed())
