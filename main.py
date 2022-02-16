import discord
import asyncio
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord_cog import DiscordCog

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
  start_em = discord.Embed(title= "Get to work!",color= 0x33c633)
  
  await ctx.send(embed = start_em)
  await asyncio.sleep(25)
  start_play_em = discord.Embed(title= "Lets play!",color= 0x44)
  await ctx.send(embed=start_play_em )
@bot.command(name="stop", help= "stops a study timer")
async def start_timer(ctx):
  stop_timer_em = discord.Embed(title= "Why did you stop the timer?", color= 0xc6333)
  await ctx.send(embed = stop_timer_em)
 #   if message.author == client.user:
  #      return
 #   if message.content.startswith('$hello'):
 #      await message.channel.send('Hello!')

#client.run(os.environ['BOT_TOKEN'])


#bot.add_cog(DiscordCog(bot))
bot.run(os.environ['BOT_TOKEN'])
