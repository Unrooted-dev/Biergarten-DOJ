import nextcord
from nextcord.ext import commands
from nextcord import Interaction

import conf.config as cfg
from views.role_request_view import RoleRequestView
from conf.permission import _is_chief_of_justice


class RoleRequestCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(RoleRequestView())
        print("✅ Rollen-Anfrage System geladen")

    # ── Hilfsmethode: Panel Embed ──────────────────────────────
    @staticmethod
    def _build_panel_embed() -> nextcord.Embed:
        embed = nextcord.Embed(
            title="📋 Rollen-Anfrage",
            description=(
                "Du möchtest eine offizielle Rolle auf diesem Server erhalten?\n\n"
                "Klicke auf den Button unten um eine **Rollen-Anfrage** zu stellen.\n"
                "Ein zuständiges Teammitglied wird sich dann schnellstmöglich bei dir melden."
            ),
            color=nextcord.Color.blurple(),
        )
        embed.set_footer(text="Biergarten DOJ • Rollen-Anfrage")
        return embed

    # ── Slash Command ──────────────────────────────────────────
    @nextcord.slash_command(
        name="role-request-panel",
        description="[Chief of Justice] Sendet oder aktualisiert das Rollen-Anfrage Panel",
    )
    async def role_request_panel(self, interaction: Interaction):
        if not _is_chief_of_justice(interaction):
            await interaction.response.send_message(
                "❌ Nur der **Chief of Justice** kann diesen Befehl nutzen.",
                ephemeral=True,
            )
            return

        channel = self.bot.get_channel(cfg.ROLE_REQUEST_CHANNEL_ID)
        embed   = self._build_panel_embed()

        if cfg.ROLE_REQUEST_PANEL_MESSAGE_ID:
            try:
                msg = await channel.fetch_message(cfg.ROLE_REQUEST_PANEL_MESSAGE_ID)
                await msg.edit(embed=embed, view=RoleRequestView())
                await interaction.response.send_message(
                    "🔄 Rollen-Anfrage Panel aktualisiert!", ephemeral=True
                )
                return
            except (nextcord.NotFound, nextcord.HTTPException):
                pass

        msg = await channel.send(embed=embed, view=RoleRequestView())
        cfg.ROLE_REQUEST_PANEL_MESSAGE_ID = msg.id
        await interaction.response.send_message(
            "✅ Rollen-Anfrage Panel gesendet!", ephemeral=True
        )


def setup(bot: commands.Bot):
    bot.add_cog(RoleRequestCog(bot))
