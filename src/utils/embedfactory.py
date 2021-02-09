import datetime
from typing import Union

import discord

BOT_NAME = "leapsong"
ICON_URL = "http://www.icon-surfer.com/wp-content/uploads/2014/02/14020912.png"


def embed_factory(
        user_display_name: str,
        user_abatar_url: str,
        user_id: int,
        key_fingerprint: Union[str, None] = None,
        key_id: Union[int, None] = None,
        valid_date: Union[datetime.datetime, None] = None,
        mode: str = "INQUIRY"
    ) -> discord.Embed:
    if mode == "INQUIRY":
        embed = __inquiry_embed(user_display_name, user_abatar_url, user_id, key_fingerprint, key_id, valid_date)
        return embed


def __inquiry_embed(
        user_display_name: str,
        user_abatar_url: str,
        user_id: int,
        key_fingerprint: Union[str, None] = None,
        key_id: Union[int, None] = None,
        valid_date: Union[datetime.datetime, None] = None
    ) -> discord.Embed:

    if key_fingerprint is None:
        # TODO: 鍵が登録されていなかった場合の処理
        title = "{} の情報".format(user_display_name)
        description = "GPG公開鍵は登録されていません" + \
                      "\n`!gpg register`で鍵を登録してください"

        embed = discord.Embed(title=title, description=description, color=0xfd3c3c)
        embed.set_author(name=BOT_NAME, icon_url=ICON_URL)
        embed.set_thumbnail(url=user_abatar_url)

        return embed

    title = "{} の情報".format(user_display_name)
    description = "GPG公開鍵が登録されています"

    key_holder_mention = "<@!{}>".format(user_id)

    parsed_valid_date = str(valid_date)
    parsed_key_id = "`{}`".format(key_id)
    parsed_fingerprint = "`{}`".format(key_fingerprint)

    embed = discord.Embed(title=title, description=description, color=0x3498DB)
    embed.set_author(name=BOT_NAME, icon_url=ICON_URL)
    embed.set_thumbnail(url=user_abatar_url)
    embed.add_field(name="鍵の所有者", value=key_holder_mention, inline=False)
    embed.add_field(name="公開鍵のID", value=parsed_key_id, inline=False)
    embed.add_field(name="フィンガープリント", value=parsed_fingerprint, inline=False)
    embed.add_field(name="有効期限", value=parsed_valid_date, inline=True)

    return embed
