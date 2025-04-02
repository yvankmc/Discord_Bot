import requests
import json
def get_meme(): # Makes function that gets data from API and returns a meme
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

def get_fact(): # Makes function that gets data from API and returns a fact about a random soccer team
  responses = requests.get("https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l=English%20Premier%20League")
  json_datas = json.loads(responses.text)
  team = json_datas['teams']
  import random
  random_team = random.choice(team)
  
  fact = f"Team: {random_team['strTeam']}\nFounded: {random_team['intFormedYear']}\nStadium: {random_team['strStadium']}\nDescription: {random_team['strDescriptionEN']}"

  return fact

import discord

class MyClient(discord.Client): # When the program is ran, it will print out how the bot is logged in onto the terminal
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message): # Makes function that creates commands for user to type with certain responses the bot can give 
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        if message.content.startswith('$fact'):
            await message.channel.send(get_fact())
    




intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Token Here') # Enter your bot token here
