import nextcord
from nextcord import ui, Interaction

import conf.config as cfg


class RoleRequestView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @ui.button(
        label="📩 Rolle anfragen",
        style=nextcord.ButtonStyle.blurple,
        custom_id="role_request:request",
    )
    async def request_role(self, button: ui.Button, interaction: Interaction):
        guild = interaction.guild
        user  = interaction.user

        role1 = guild.get_role(cfg.ROLE_REQUEST_PING_ROLE_1)
        role2 = guild.get_role(cfg.ROLE_REQUEST_PING_ROLE_2)

        # Pings zusammenstellen (nur vorhandene Rollen)
        pings = " ".join(r.mention for r in [role1, role2] if r)

        # Embed für die gepingten Rollen
        embed = nextcord.Embed(
            title="📩 Neue Rollen-Anfrage",
            description=(
                f"{user.mention} möchte eine Rolle beantragen.\n\n"
                f"Bitte meldet euch bei dem Mitglied."
            ),
            color=nextcord.Color.blurple(),
        )
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.add_field(name="👤 Mitglied", value=f"{user.mention} (`{user}`)", inline=False)
        embed.set_footer(text="Biergarten DOJ • Rollen-Anfrage")

        # Nachricht im selben Channel senden (öffentlich für die Pings)
        await interaction.channel.send(
            content=pings,
            embed=embed,
            allowed_mentions=nextcord.AllowedMentions(roles=True),
        )

        # Bestätigung ephemeral an den User
        await interaction.response.send_message(
            "✅ Deine Anfrage wurde abgeschickt! Das Team wird sich bei dir melden.",
            ephemeral=True,
        )
