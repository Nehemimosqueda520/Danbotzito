import discord
import os
from dotenv import load_dotenv
from src.AI import client as ai_client

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)  

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    

    if message.content.startswith('d!t'):
        await message.channel.send(
            ai_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=message.content[4:],
            ).text
        )

client.run(os.getenv('BOT_TOKEN'))