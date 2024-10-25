import asyncio
import discord
from discord.ext import commands
from discord import app_commands

async def main():
    TOKEN = "[YOUR TOKEN HERE]" # Homework: Load from a .env file, since putting tokens in code is bad practice

    # BOT SETUP
    intents = discord.Intents.all()
    intents.message_content = True  # Enable the message content intent
    intents.members = True  # Enable the message content intent
    bot = commands.Bot(command_prefix="!", intents=intents)  # Set a command prefix

    # Event to show bot is ready
    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')

        await bot.tree.sync()
    
    # Run the bot
    await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())