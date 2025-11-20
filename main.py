import discord
import os
from dotenv import load_dotenv
from src.AI import client as ai_client, generate_response
from src.facts import fetch_fact 

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
        print ("Generating AI response...")
        await message.channel.send(
            await generate_response(message.content[3:])       
        )

    # TODO: Implement facts command
    if message.content.startswith('d!facts'):
        print ("Fetching a random fact...")
        await message.channel.send(
            await fetch_fact()
        )
        
print("Bot is running...")

client.run(os.getenv('BOT_TOKEN'))