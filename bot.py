import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Required to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}! 👋")

@bot.command()
async def roll(ctx):
    import random
    await ctx.send(f"🎲 You rolled a {random.randint(1, 6)}!")

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run("YOUR_BOT_TOKEN")

