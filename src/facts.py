import asyncio
import aiohttp
from dotenv import load_dotenv
import os

load_dotenv()

FACTS_API_URL = os.getenv('FACTS_API_URL')

async def fetch_fact():
    async with aiohttp.ClientSession() as session:
        async with session.get(FACTS_API_URL) as response:
            if response.status == 200:
                data = await response.json()
                return data.get('text', 'No fact found.')
            else:
                return 'Failed to retrieve fact.'