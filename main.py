import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from StudyBot.discord_cog import DiscordCog

load_dotenv()
bot = commands.Bot(command_prefix='!', help_command=None)

#client = discord.Client()

#@client.event
@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))

#@client.event
@bot.command(name="start", help= "starts a study timer")
async def start_timer(ctx):
  await ctx.send("time to work!")
 #   if message.author == client.user:
  #      return
 #   if message.content.startswith('$hello'):
 #      await message.channel.send('Hello!')

#client.run(os.environ['BOT_TOKEN'])


#bot.add_cog(DiscordCog(bot))
bot.run(os.environ['BOT_TOKEN'])
