from nextcord import Interaction
import conf.config as cfg


def _is_chief_of_justice(interaction: Interaction) -> bool:
    """Prüft ob der User die Chief of Justice Rolle hat."""
    role = interaction.guild.get_role(cfg.CHIEF_OF_JUSTICE_ROLE_ID)
    return role in interaction.user.roles if role else False