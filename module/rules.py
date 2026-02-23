import nextcord
from nextcord.ext import commands
from nextcord import Interaction

import conf.config as cfg
from views.rules_view import RulesView
from conf.permission import _is_chief_of_justice


class RulesCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(RulesView())
        print("✅ Rules System geladen")

    # ── Hilfsmethoden ─────────────────────────────────────────
    @staticmethod
    def _build_rules_embed() -> nextcord.Embed:
        embed = nextcord.Embed(
            title="📜 Serverregeln",
            description=(
                "Willkommen auf dem **Biergarten DOJ** Server!\n"
                "Bitte beachte folgende Regeln für ein angenehmes Miteinander.\n\n"
                "**1️⃣ Respekt**\n"
                "Behandle alle Mitglieder mit Respekt und Höflichkeit.\n"
                "Diskriminierung, Beleidigungen oder Belästigungen werden nicht toleriert.\n\n"
                "**2️⃣ Keine illegalen Inhalte**\n"
                "Das Teilen von illegalen Inhalten ist streng verboten.\n\n"
                "**3️⃣ Keine Werbung**\n"
                "Werbung für andere Server oder Produkte ist ohne Erlaubnis nicht gestattet.\n\n"
                "**4️⃣ Richtige Kanäle nutzen**\n"
                "Poste Inhalte nur in den dafür vorgesehenen Kanälen.\n\n"
                "**5️⃣ Keine Spoiler ohne Warnung**\n"
                "Verwende Spoiler-Tags für entsprechende Inhalte.\n\n"
                "**6️⃣ Moderation respektieren**\n"
                "Folge den Anweisungen des Moderationsteams.\n\n"
                "**7️⃣ Roleplay-Regeln**\n"
                "IC (In Character) und OOC (Out of Character) sind strikt zu trennen.\n"
                "Powergaming, Metagaming und RDM sind verboten."
            ),
            color=nextcord.Color.blurple(),
        )
        embed.set_footer(text="Biergarten DOJ • Regeln")
        return embed

    @staticmethod
    def _build_roles_embed(guild: nextcord.Guild) -> nextcord.Embed:
        embed = nextcord.Embed(
            title="👥 Rollen-Übersicht",
            description="Hier findest du alle offiziellen Rollen des Servers und ihre Zuständigkeiten.",
            color=nextcord.Color.gold(),
        )
        for entry in cfg.ROLE_DESCRIPTIONS:
            role = guild.get_role(entry["role_id"])
            mention = role.mention if role else f"`{entry['label']}`"
            embed.add_field(
                name=f"{entry['emoji']}  {entry['label']}",
                value=f"{mention}\n{entry['description']}",
                inline=False,
            )
        embed.set_footer(text="Biergarten DOJ • Rollen")
        return embed

    # ── Slash Commands ────────────────────────────────────────
    @nextcord.slash_command(
        name="rules-panel",
        description="[Chief of Justice] Sendet oder aktualisiert das Regelwerk-Panel",
    )
    async def rules_panel(self, interaction: Interaction):
        if not _is_chief_of_justice(interaction):
            await interaction.response.send_message(
                "❌ Nur der **Chief of Justice** kann diesen Befehl nutzen.", ephemeral=True
            )
            return

        channel = self.bot.get_channel(cfg.RULES_CHANNEL_ID)
        embed   = self._build_rules_embed()

        if cfg.RULES_PANEL_MESSAGE_ID:
            try:
                msg = await channel.fetch_message(cfg.RULES_PANEL_MESSAGE_ID)
                await msg.edit(embed=embed, view=RulesView())
                await interaction.response.send_message("🔄 Regelwerk aktualisiert!", ephemeral=True)
                return
            except (nextcord.NotFound, nextcord.HTTPException):
                pass

        msg = await channel.send(embed=embed, view=RulesView())
        cfg.RULES_PANEL_MESSAGE_ID = msg.id
        await interaction.response.send_message("✅ Regelwerk gesendet!", ephemeral=True)

    @nextcord.slash_command(
        name="roles-panel",
        description="[Chief of Justice] Sendet oder aktualisiert die Rollen-Übersicht",
    )
    async def roles_panel(self, interaction: Interaction):
        if not _is_chief_of_justice(interaction):
            await interaction.response.send_message(
                "❌ Nur der **Chief of Justice** kann diesen Befehl nutzen.", ephemeral=True
            )
            return

        channel = self.bot.get_channel(cfg.ROLES_CHANNEL_ID)
        embed   = self._build_roles_embed(interaction.guild)

        if cfg.ROLES_PANEL_MESSAGE_ID:
            try:
                msg = await channel.fetch_message(cfg.ROLES_PANEL_MESSAGE_ID)
                await msg.edit(embed=embed)
                await interaction.response.send_message("🔄 Rollen-Übersicht aktualisiert!", ephemeral=True)
                return
            except (nextcord.NotFound, nextcord.HTTPException):
                pass

        msg = await channel.send(embed=embed)
        cfg.ROLES_PANEL_MESSAGE_ID = msg.id
        await interaction.response.send_message("✅ Rollen-Übersicht gesendet!", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(RulesCog(bot))
