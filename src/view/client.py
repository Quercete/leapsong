import asyncio
import os
from typing import Union

import discord

from src.view.on_message.root import message_root
from config import DISCORD_TOKEN

TEST_TEXT_CH_ID = 711127633810817026


class MainClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.TEST_TEXT_CH: Union[None, discord.TextChannel] = None

    def run(self):
        super().run(DISCORD_TOKEN)

    async def on_ready(self):
        self.TEST_TEXT_CH = self.get_channel(TEST_TEXT_CH_ID)

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        await message_root(message)
