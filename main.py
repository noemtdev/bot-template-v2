from src.bot import create_bot
from quart import Quart
from quart_cors import cors
import os

app = Quart(__name__)
app = cors(app, allow_origin="*")

METHODS = ["GET", "POST"]

for METHOD in METHODS:
    for file in os.listdir(f"src/api/{METHOD}"):
        if file.endswith(".py"):
            
            route = __import__(f"src.api.{METHOD}.{file[:-3]}", fromlist=["route", "func"])
            endpoint = f"{METHOD}_{file[:-3]}"

            app.add_url_rule(route.route, endpoint, route.func, methods=[METHOD])
            print(f"Added route {route.route} with method {METHOD}.")

if __name__ == "__main__":
    bot = create_bot()
    bot.run(app, 1337)
