import os
import discord
import requests
import json
#import random
from app import keep_alive
 
# variables
discord_client = discord.Client()
DB_Token = os.environ['DB-TOKEN']
NASA_API_KEY = os.environ['NASA-API-KEY']

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#----- For Fun ---------------
def yes_no():
  response = requests.get("https://yesno.wtf/api/")
  json_data = json.loads(response.text)
  return json_data["answer"] , json_data["image"]

def kanye_rest():
  response = requests.get("https://api.kanye.rest/")
  json_data = json.loads(response.text)
  return json_data["quote"]

#----- NASA Functions --------
def nasa_apod():
  response = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + NASA_API_KEY)
  json_data = json.loads(response.text)
  return json_data['title'] , json_data['url'] , json_data['date'], json_data['explanation']

def bored():
  response = requests.get("http://www.boredapi.com/api/activity/")
  json_data = json.loads(response.text)
  return json_data["type"] , json_data["activity"]

#apod()
# def get_norm_joke():
#   url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
#   headers = {
#       'accept': "application/json",
#       'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
#       'x-rapidapi-key': "53572b29b7mshbf323f61903a0a1p13b7a3jsna81ab2e2ca2b"
#       }
#   response = requests.request("GET", url, headers=headers)
#   print(response.text)

@discord_client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(discord_client))

@discord_client.event
async def on_message(message):
  if message.author == discord_client.user:
    return

  msg = message.content
  
  if '$inspire' in msg:
    quote = get_quote()
    await message.channel.send(quote)

  #------- For Fun
  if '$yes/no' in msg:
    answer, image = yes_no()
    await message.channel.send("WALL-E Says: " + answer.capitalize()  + "\n" + image)

  if '$kanye-rest' in msg:
    quote = kanye_rest()
    await message.channel.send(quote + " -Kanye West")

  #-------- Educational/Helpful/Interesting
  if '$nasa-apod' in msg:
    title, url, date, explanation = nasa_apod()
    await message.channel.send(title + "\n" + url + "\n" + explanation)

  if '$bored' in msg:
    type, activity = bored()
    await message.channel.send("```txt\nWALL-E suggests...\n\nActivity: " + activity + "\n" + "Type: " + type.capitalize() + "```")

# keeps on pinging the bot and keeps it running 24/7
keep_alive()
discord_client.run(DB_Token)