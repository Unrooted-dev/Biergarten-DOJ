from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from nextcord import Intents
import os
from dotenv import load_dotenv


load_dotenv()

intents = Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents.all())