import nextcord
from nextcord import ui, Interaction

from conf.config import TICKET_CATEGORIES, JUDGE_ROLE_ID, PROSECUTOR_ROLE_ID, CHIEF_OF_JUSTICE_ROLE_ID, ATTORNEY_ROLE_ID


# ─────────────────────────────────────────────
#  Dropdown  –  Kategorie auswählen
# ─────────────────────────────────────────────
class TicketCategorySelect(ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label=cat["label"],
                emoji=cat["emoji"],
                description=cat["description"],
                value=cat["value"],
            )
            for cat in TICKET_CATEGORIES
        ]
        super().__init__(
            placeholder="📂  Wähle eine Kategorie …",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="ticket:select",
        )

    async def callback(self, interaction: Interaction):
        value = self.values[0]
        guild = interaction.guild
        user  = interaction.user

        # Kategorie aus Config holen
        category = next((c for c in TICKET_CATEGORIES if c["value"] == value), None)
        if not category:
            await interaction.response.send_message("❌ Ungültige Kategorie.", ephemeral=True)
            return

        # Bereits offenes Ticket prüfen
        channel_name = f"ticket-{user.name.lower()}-{value}"
        existing = nextcord.utils.get(guild.text_channels, name=channel_name)
        if existing:
            await interaction.response.send_message(
                f"❌ Du hast bereits ein offenes Ticket: {existing.mention}",
                ephemeral=True,
            )
            return

        # Permissions
        support_roles  = [
            guild.get_role(JUDGE_ROLE_ID),
            guild.get_role(PROSECUTOR_ROLE_ID),
            guild.get_role(CHIEF_OF_JUSTICE_ROLE_ID),
            guild.get_role(ATTORNEY_ROLE_ID)
        ]
        category_role = guild.get_role(category["role_id"])
        overwrites = {
            guild.default_role: nextcord.PermissionOverwrite(view_channel=False),
            user: nextcord.PermissionOverwrite(
                view_channel=True, send_messages=True, read_message_history=True
            ),
        }
        for support_role in support_roles:
            if support_role:
                overwrites[support_role] = nextcord.PermissionOverwrite(
                    view_channel=True, send_messages=True, read_message_history=True
                )
        if category_role and category_role not in support_roles:
            overwrites[category_role] = nextcord.PermissionOverwrite(
                view_channel=True, send_messages=True, read_message_history=True
            )

        # Channel anlegen
        channel = await guild.create_text_channel(
            name=channel_name,
            overwrites=overwrites,
            reason=f"Ticket [{category['label']}] von {user}",
        )

        # Ping & Embed im Ticket-Channel
        ping_role = category_role or support_role
        await channel.send(
            content=f"{ping_role.mention if ping_role else ''} | {user.mention}",
            allowed_mentions=nextcord.AllowedMentions(roles=True, users=True),
        )

        embed = nextcord.Embed(
            title=f"{category['emoji']}  {category['label']}",
            description=(
                f"Willkommen {user.mention}!\n"
                f"Beschreibe dein Anliegen und wir melden uns so schnell wie möglich."
            ),
            color=nextcord.Color.blurple(),
        )
        embed.set_footer(text="Zum Schließen → Button unten drücken")
        await channel.send(embed=embed, view=TicketCloseView())

        await interaction.response.send_message(
            f"✅ Ticket erstellt: {channel.mention}", ephemeral=True
        )


# ─────────────────────────────────────────────
#  Panel View  –  wird im Support-Channel gepostet
# ─────────────────────────────────────────────
class TicketCreateView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(TicketCategorySelect())


# ─────────────────────────────────────────────
#  Close View  –  wird im Ticket-Channel gepostet
# ─────────────────────────────────────────────
class TicketCloseView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @ui.button(
        label="🔒 Ticket schließen",
        style=nextcord.ButtonStyle.red,
        custom_id="ticket:close",
    )
    async def close_ticket(self, button: ui.Button, interaction: Interaction):
        embed = nextcord.Embed(
            title="🔒 Ticket wird geschlossen",
            description=f"Geschlossen von {interaction.user.mention}",
            color=nextcord.Color.red(),
        )
        await interaction.response.send_message(embed=embed)
        await interaction.channel.delete(
            reason=f"Ticket geschlossen von {interaction.user}"
        )
