import discord
import handle
from dotenv import load_dotenv
import os

from dotenv import load_dotenv

dotenv_path = os.join(os.dirname(__file__), '.env')
load_dotenv(dotenv_path)

async def sendMessage(msg, userMsg):
    try:
        response = handle.responseHandler(userMsg)
        await msg.channel.send(response)
    except Exception as e:
        print(e)

def runBot():
    TOKEN = os.environ.get("TOKEN")
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is running')
    
    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return
        
        username = str(msg.author)
        userMessage = str(msg.content)
        channel = str(msg.channel)

        print(f'{username}, {userMessage}, {channel}')
        await sendMessage(msg, userMsg=userMessage)

    client.run(TOKEN)