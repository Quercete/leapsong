import asyncio
import os

import discord

TOKEN = os.getenv("TOKEN")


class MainClient(discord.Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        pass

    def run(self):
        super().run(TOKEN)

    async def on_message(self, message: discord.Message):
        pass
