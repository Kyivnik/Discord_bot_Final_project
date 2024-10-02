import discord
import requests
import json
import my_api
from my_api import api


def get_joke():
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    json_data = json.loads(response.text)

    if json_data['type'] == 'twopart':
        return f"{json_data['setup']} - {json_data['delivery']}"
    else:
        return json_data['joke']


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Ignore the bot's own messages
        if message.author == self.user:
            return

        if message.content.startswith('$joke'):
            joke = get_joke()
            await message.channel.send(joke)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run(api)


