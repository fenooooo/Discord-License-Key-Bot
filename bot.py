
import os
import discord
import random
import string
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX", "!")

# Set up the bot
bot = commands.Bot(command_prefix=PREFIX)

# In-memory storage for license keys (could be saved in a file or database)
license_keys = []

# Function to generate a random license key
def generate_license_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

@bot.event
async def on_ready():
    print(f"Logged in as {{bot.user}}")

@bot.command(name='genkey', help="Generates a new license key.")
@commands.has_permissions(administrator=True)
async def generate_key(ctx):
    key = generate_license_key()
    license_keys.append(key)
    await ctx.send(f"New license key generated: {key}")

@bot.command(name='verifykey', help="Verifies if a license key is valid.")
async def verify_key(ctx, key):
    if key in license_keys:
        await ctx.send(f"License key {key} is valid!")
    else:
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        await ctx.send(f"License key {key} is invalid! Would you like to generate a key for this user? (yes/no)")
        
        try:
            msg = await bot.wait_for("message", check=check, timeout=30.0)
            if msg.content.lower() == "yes":
                new_key = generate_license_key()
                license_keys.append(new_key)
                await ctx.send(f"New key generated: {new_key}")
            else:
                await ctx.send("License request denied.")
        except Exception as e:
            await ctx.send("Request timed out or an error occurred.")

bot.run(TOKEN)
