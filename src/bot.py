import discord
from discord.ext import commands
import os
import logging

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.command_prefix = ">"
        self.load_commands()

        self.logger = logging.getLogger("discord")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
        handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
        self.logger.addHandler(handler)

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    def load_commands(self):
        for filename in os.listdir("src/cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"src.cogs.{filename[:-3]}")

    def run(self, app, port):
        token = os.getenv("authorization")
        self.loop.create_task(self.start(token))
        self.loop.create_task(app.run_task("0.0.0.0", port=port))
        self.loop.run_forever()

def create_bot():
    intents = discord.Intents.default()
    bot = Bot(command_prefix="!", intents=intents)

    return bot