import os, discord, time, json
from dotenv import load_dotenv
from discord.ext import commands, bridge
os.system('cls' if os.name == 'nt' else 'clear')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

with open("config.json", "r") as f:
    config = json.load(f)

if __name__ == "__main__":
    print(f"Working directory: {os.getcwd()}")
    time_log = {"start": None, "ready": None}
    bot = bridge.Bot(command_prefix= config["prefix"], intents= discord.Intents.all())

    #Load commands
    for extension in config["extensions"]:
        bot.load_extension(f"commands.{extension}")

    #On bot startup
    time_log["start"] = time.time()

    @bot.event
    async def on_ready():
        #Setting the bot status
        await bot.change_presence(
            status= discord.Status.do_not_disturb,
            activity= discord.Activity(
                type= discord.ActivityType.playing,
                name= "with your life."
            )
        )

        #Logging
        time_log["ready"] = round(time.time() - time_log["start"], 4)
        print(f"Bot is up and running as {bot.user} after {time_log['ready']} seconds")

    bot.run(TOKEN)