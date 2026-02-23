import nextcord
from nextcord.ext import commands

import conf.config as cfg


class WelcomeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        channel = self.bot.get_channel(cfg.WELCOME_CHANNEL_ID)
        if not channel:
            return

        embed = nextcord.Embed(
            title=f"👋 Willkommen auf {member.guild.name}!",
            description=(
                f"Hey {member.mention}, Willkommen auf dem Biergarten DOJ server!\n\n"
                f"Schau dich um, lies die Regeln und hab Spaß 🎉"
            ),
            color=nextcord.Color.blurple(),
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="👤 Mitglied", value=str(member), inline=True)
        embed.add_field(
            name="🔢 Mitglied #",
            value=str(member.guild.member_count),
            inline=True,
        )
        embed.set_footer(text="Biergarten DOJ • Welcome")

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("✅ Welcome System geladen")


def setup(bot: commands.Bot):
    bot.add_cog(WelcomeCog(bot))
