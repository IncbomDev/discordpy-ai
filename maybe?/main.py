import discord
import os
from neuralintents import GenericAssistant
from dotenv import load_dotenv
client = discord.Client()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()


print("Bot is ready")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Saibot'):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)


client.run(TOKEN)