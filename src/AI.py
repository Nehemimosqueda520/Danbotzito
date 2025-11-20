from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key = os.getenv("AI_API_KEY")
)

prompt = "you're a discord bot called danbotzito, be funny and short when responding to users. your messages will be less than 4000 characters. you will speak english or spanish depending of the message"

async def generate_response(user_input: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= "prompt: " + prompt + "\n\nUsuario: " + user_input
    )
    return response.text 