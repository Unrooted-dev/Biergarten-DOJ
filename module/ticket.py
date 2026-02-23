import nextcord
from nextcord.ext import commands
from nextcord import Interaction

import conf.config as cfg
from views.ticket_view import TicketCreateView


class TicketCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(TicketCreateView())
        self.bot.add_view(__import__("views.ticket_view", fromlist=["TicketCloseView"]).TicketCloseView())
        print("✅ Ticket System geladen")

    # ── Hilfsmethode: Panel Embed bauen ──────────────────────
    @staticmethod
    def _build_panel_embed() -> nextcord.Embed:
        embed = nextcord.Embed(
            title="🎫 Support Ticket",
            description=(
                "Wähle eine Kategorie aus dem Dropdown um ein Ticket zu öffnen.\n"
                "Die jeweilige Stelle wird sich schnellstmöglich bei dir melden.\n\n"
                "**Kategorien**\n"
                + "\n".join(
                    f"{cat['emoji']} **{cat['label']}** — {cat['description']}"
                    for cat in cfg.TICKET_CATEGORIES
                )
            ),
            color=nextcord.Color.blurple(),
        )
        embed.set_footer(text="Biergarten DOJ • Support")
        return embed

    # ── Slash Command ─────────────────────────────────────────
    @nextcord.slash_command(name="ticket-panel", description="Sendet oder aktualisiert das Ticket Panel")
    async def ticket_panel(self, interaction: Interaction):
        channel = self.bot.get_channel(cfg.CHANNEL_ID)
        embed   = self._build_panel_embed()

        # Bestehendes Panel updaten, sonst neu senden
        if cfg.PANEL_MESSAGE_ID:
            try:
                msg = await channel.fetch_message(cfg.PANEL_MESSAGE_ID)
                await msg.edit(embed=embed, view=TicketCreateView())
                await interaction.response.send_message("🔄 Panel aktualisiert!", ephemeral=True)
                return
            except (nextcord.NotFound, nextcord.HTTPException):
                pass  # Nachricht nicht mehr vorhanden → neu senden

        msg = await channel.send(embed=embed, view=TicketCreateView())
        cfg.PANEL_MESSAGE_ID = msg.id
        await interaction.response.send_message("✅ Panel gesendet!", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(TicketCog(bot))
