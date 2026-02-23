import nextcord

from conf.bot import bot
from conf.config import DISCORD_TOKEN

# ── Cogs laden ────────────────────────────────────────────────
bot.load_extension("module.ticket")
bot.load_extension("module.welcome")


@bot.slash_command(name="ping", description="Check the bot's latency")
async def ping(interaction: nextcord.Interaction):
    latency = bot.latency * 1000
    await interaction.response.send_message(f"🏓 Pong! `{latency:.2f} ms`", ephemeral=True)


bot.run(DISCORD_TOKEN)
