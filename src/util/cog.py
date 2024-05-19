from discord.ext import commands
from src.constants.constants import some_important_constant

class Cog(commands.Cog):
    def __init__(self):
        self.important_constant = some_important_constant