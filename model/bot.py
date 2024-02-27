import dicord
import asyncio
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('toker')

intents = discord.Intents.default()
intents.message_content = True

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="FF15"))
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print("erreur")
        print(e)

    print('------')

    bot.run(token)

