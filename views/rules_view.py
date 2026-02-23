import nextcord
from nextcord import ui, Interaction


class RulesView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)
