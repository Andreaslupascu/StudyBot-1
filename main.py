import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from StudyBot.discord_cog import DiscordCog

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.environ['BOT_TOKEN'])


bot = commands.Bot(command_prefix='!', help_command=None)
bot.add_cog(DiscordCog(bot))
bot.run(os.environ['BOT_TOKEN'])
