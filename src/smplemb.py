import discord


# TODO: そのうち闇に葬る
def sample_embed():
    embed = discord.Embed(title="†マクスウェルのこるく† の情報", description="GPG公開鍵が登録されています", color=0x3498DB)

    embed.set_author(name="leapsong", icon_url = "http://www.icon-surfer.com/wp-content/uploads/2014/02/14020912.png")
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1169123537694670848/v8CyhZVU_400x400.jpg")
    embed.add_field(name="鍵の所有者", value="<@!554985192549515264>", inline=False)
    embed.add_field(name="公開鍵のID", value="`17CF 9C20 46CF 1B67`", inline=False)
    embed.add_field(name="フィンガープリント", value="`E27E 14ED 6771 02F5 051D 6E31 C046 9D56 0DE4 1848`", inline=False)
    embed.add_field(name="有効期限", value="2023/06/02 08:91:13 (GMT +0900)", inline=True)

    return embed
