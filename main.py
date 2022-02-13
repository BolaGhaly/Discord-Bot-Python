import os
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
RSA_KEY = os.environ['RSA-KEY']
A_KEY = os.environ['a-rapidapi-key']
A_HOST = os.environ['a-rapidapi-host']


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


#------- For Fun
def yes_no():
    response = requests.get("https://yesno.wtf/api/")
    json_data = json.loads(response.text)
    return json_data["answer"], json_data["image"]


def kanye_rest():
    response = requests.get("https://api.kanye.rest/")
    json_data = json.loads(response.text)
    return json_data["quote"]


#-------- Educational/Helpful/Interesting
def nasa_apod():
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=" +
                            NASA_API_KEY)
    json_data = json.loads(response.text)
    return json_data['title'], json_data['url'], json_data['date'], json_data[
        'explanation']


def bored():
    response = requests.get("http://www.boredapi.com/api/activity/")
    json_data = json.loads(response.text)
    return json_data["type"], json_data["activity"]


def fake_person_female():
    response = requests.get(
        "https://fakerapi.it/api/v1/persons?_quantity=1&_locale=en_US&_gender=female"
    )
    json_data = json.loads(response.text)
    firstname = json_data["data"][0]['firstname']
    lastname = json_data["data"][0]['lastname']
    name = firstname + " " + lastname
    gender = json_data["data"][0]['gender']
    birthday = json_data["data"][0]['birthday']
    phone = json_data["data"][0]['phone']
    email = json_data["data"][0]['email']
    address = json_data["data"][0]['address']["street"]
    return (name, gender, birthday, phone, email, address)


def fake_person_male():
    response = requests.get(
        "https://fakerapi.it/api/v1/persons?_quantity=1&_locale=en_US&_gender=male"
    )
    json_data = json.loads(response.text)
    firstname = json_data["data"][0]['firstname']
    lastname = json_data["data"][0]['lastname']
    name = firstname + " " + lastname
    gender = json_data["data"][0]['gender']
    birthday = json_data["data"][0]['birthday']
    phone = json_data["data"][0]['phone']
    email = json_data["data"][0]['email']
    address = json_data["data"][0]['address']["street"]
    return (name, gender, birthday, phone, email, address)


def fake_credit_Card():
    response = requests.get(
        "https://fakerapi.it/api/v1/credit_cards?_quantity=1")
    json_data = json.loads(response.text)
    type = json_data["data"][0]['type']
    number = json_data["data"][0]['number']
    expiration = json_data["data"][0]['expiration']
    owner = json_data["data"][0]['owner']
    return (type, owner, number, expiration)


def next_marvel_movie():
    response = requests.get("https://whenisthenextmcufilm.com/api")
    json_data = json.loads(response.text)
    title_1 = json_data['title']
    days_until_1 = json_data['days_until']
    release_date_1 = json_data['release_date']
    type_1 = json_data['type']
    overview_1 = json_data['overview']
    poster_url_1 = json_data['poster_url']

    return (title_1, days_until_1, release_date_1, type_1, overview_1,
            poster_url_1)


def next_marvel_movie_afterwards():
    response = requests.get("https://whenisthenextmcufilm.com/api")
    json_data = json.loads(response.text)
    title = json_data["following_production"]['title']
    days_until = json_data["following_production"]['days_until']
    release_date = json_data["following_production"]['release_date']
    type = json_data["following_production"]['type']
    overview = json_data["following_production"]['overview']
    poster_url = json_data["following_production"]['poster_url']

    return (title, days_until, release_date, type, overview, poster_url)


def anime_happy_gif():
    url = "https://random-stuff-api.p.rapidapi.com/anime/happy"
    querystring = {"limit": "1"}
    headers = {
        'authorization': RSA_KEY,
        'x-rapidapi-host': A_HOST,
        'x-rapidapi-key': A_KEY
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    json_data = json.loads(response.text)
    return (json_data[0]["url"])


def anime_hi_gif():
    url = "https://random-stuff-api.p.rapidapi.com/anime/hi"
    querystring = {"limit": "1"}
    headers = {
        'authorization': RSA_KEY,
        'x-rapidapi-host': A_HOST,
        'x-rapidapi-key': A_KEY
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    json_data = json.loads(response.text)
    return (json_data[0]["url"])


def anime_kiss_gif():
    url = "https://random-stuff-api.p.rapidapi.com/anime/kiss"
    querystring = {"limit": "1"}
    headers = {
        'authorization': RSA_KEY,
        'x-rapidapi-host': A_HOST,
        'x-rapidapi-key': A_KEY
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    json_data = json.loads(response.text)
    return (json_data[0]["url"])


def anime_hug_gif():
    url = "https://random-stuff-api.p.rapidapi.com/anime/hug"
    querystring = {"limit": "1"}
    headers = {
        'authorization': RSA_KEY,
        'x-rapidapi-host': A_HOST,
        'x-rapidapi-key': A_KEY
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    json_data = json.loads(response.text)
    return (json_data[0]["url"])


def anime_punch_gif():
    url = "https://random-stuff-api.p.rapidapi.com/anime/punch"
    querystring = {"limit": "1"}
    headers = {
        'authorization': RSA_KEY,
        'x-rapidapi-host': A_HOST,
        'x-rapidapi-key': A_KEY
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    json_data = json.loads(response.text)
    return (json_data[0]["url"])


def anime_pat_gif():
    url = "https://random-stuff-api.p.rapidapi.com/anime/pat"
    querystring = {"limit": "1"}
    headers = {
        'authorization': RSA_KEY,
        'x-rapidapi-host': A_HOST,
        'x-rapidapi-key': A_KEY
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    json_data = json.loads(response.text)
    return (json_data[0]["url"])

def anime_slap_gif():
    url = "https://random-stuff-api.p.rapidapi.com/anime/slap"
    querystring = {"limit": "1"}
    headers = {
        'authorization': RSA_KEY,
        'x-rapidapi-host': A_HOST,
        'x-rapidapi-key': A_KEY
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    json_data = json.loads(response.text)
    return (json_data[0]["url"])

def anime_nervous_gif():
    url = "https://random-stuff-api.p.rapidapi.com/anime/nervous"
    querystring = {"limit": "1"}
    headers = {
        'authorization': RSA_KEY,
        'x-rapidapi-host': A_HOST,
        'x-rapidapi-key': A_KEY
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    json_data = json.loads(response.text)
    return (json_data[0]["url"])

def anime_run_gif():
    url = "https://random-stuff-api.p.rapidapi.com/anime/run"
    querystring = {"limit": "1"}
    headers = {
        'authorization': RSA_KEY,
        'x-rapidapi-host': A_HOST,
        'x-rapidapi-key': A_KEY
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    json_data = json.loads(response.text)
    return (json_data[0]["url"])


def anime_cry_gif():
    url = "https://random-stuff-api.p.rapidapi.com/anime/cry"
    querystring = {"limit": "1"}
    headers = {
        'authorization': RSA_KEY,
        'x-rapidapi-host': A_HOST,
        'x-rapidapi-key': A_KEY
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    json_data = json.loads(response.text)
    return (json_data[0]["url"])


@discord_client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(discord_client))


@discord_client.event
async def on_message(message):
    if message.author == discord_client.user:
        return

    msg = message.content

    if msg == '$inspire':
        quote = get_quote()
        await message.channel.send(quote)

    #------- For Fun
    if msg == '$yes/no':
        answer, image = yes_no()
        await message.channel.send("WALL-E Says: " + answer.capitalize() +
                                   "\n" + image)

    if msg == '$kanye-rest':
        quote = kanye_rest()
        await message.channel.send(quote + " -Kanye West")

    #-------- Educational/Helpful/Interesting
    if msg == '$nasa-apod':
        title, url, date, explanation = nasa_apod()
        await message.channel.send(title + "\n" + url + "\n" + explanation)

    if msg == '$bored':
        type, activity = bored()
        await message.channel.send("```txt\nWALL-E suggests...\n\nActivity: " +
                                   activity + "\n" + "Type: " +
                                   type.capitalize() + "```")

    if msg == '$fake-person-male':
        name, gender, birthday, phone, email, address = fake_person_male()
        await message.channel.send("```txt\nName: " + name + "\nGender: " +
                                   gender.capitalize() + "\nBirthday: " +
                                   birthday + "\nPhone: " + phone +
                                   "\nEmail: " + email + "\nAddress: " +
                                   address + "```")

    if msg == '$fake-person-female':
        name, gender, birthday, phone, email, address = fake_person_female()
        await message.channel.send("```txt\nName: " + name + "\nGender: " +
                                   gender.capitalize() + "\nBirthday: " +
                                   birthday + "\nPhone: " + phone +
                                   "\nEmail: " + email + "\nAddress: " +
                                   address + "```")

    if msg == '$fake-credit-card':
        type, owner, number, expiration = fake_credit_Card()
        await message.channel.send("```txt\nCard Type: " + type +
                                   "\nCardholder Name: " + owner +
                                   "\nCard Number: " + number +
                                   "\nExpiration Date (mm/yy): " + expiration +
                                   "```")

    if msg == '$upcoming-marvel':
        title_1, days_until_1, release_date_1, type_1, overview_1, poster_url_1 = next_marvel_movie(
        )
        title_2, days_until_2, release_date_2, type_2, overview_2, poster_url_2 = next_marvel_movie_afterwards(
        )
        output_1 = (title_1 + " releases in " + str(days_until_1) +
                    " days!\n\nRelease Date: " + release_date_1 +
                    "\n\nProduction Type: " + type_1 + "\n\nOverview: " +
                    overview_1 + "\n")
        output_2 = (title_2 + " releases in " + str(days_until_2) +
                    " days!\n\nRelease Date: " + release_date_2 +
                    "\n\nProduction Type: " + type_2 + "\n\nOverview: " +
                    overview_2 + "\n")
        red_embed_1 = discord.Embed(
            color=0xff0000,
            title=
            "When is the next Marvel Cinematic Universe (MCU) movie/tv show?",
            description=output_1)
        red_embed_1.set_thumbnail(url=poster_url_1)
        red_embed_1.set_footer(
            text="Source (Not my website): https://whenisthenextmcufilm.com/")
        await message.channel.send(embed=red_embed_1)
        red_embed_2 = discord.Embed(
            color=0xff0000,
            title="What's afterwards? you might ask...",
            description=output_2)
        red_embed_2.set_thumbnail(url=poster_url_2)
        red_embed_2.set_footer(
            text="Source (Not my website): https://whenisthenextmcufilm.com/")
        await message.channel.send(embed=red_embed_2)

    #-------- Anime
    if msg == '$anime-happy':
        gif_url = anime_happy_gif()
        await message.channel.send(gif_url)

    if msg == '$anime-hi':
        gif_url = anime_hi_gif()
        await message.channel.send(gif_url)

    if msg == '$anime-kiss':
        gif_url = anime_kiss_gif()
        await message.channel.send(gif_url)

    if msg == '$anime-hug':
        gif_url = anime_hug_gif()
        await message.channel.send(gif_url)

    if msg == '$anime-punch':
        gif_url = anime_punch_gif()
        await message.channel.send(gif_url)

    if msg == '$anime-pat':
        gif_url = anime_pat_gif()
        await message.channel.send(gif_url)

    if msg == '$anime-slap':
        gif_url = anime_slap_gif()
        await message.channel.send(gif_url)

    if msg == '$anime-nervous':
        gif_url = anime_nervous_gif()
        await message.channel.send(gif_url)

    if msg == '$anime-run':
        gif_url = anime_run_gif()
        await message.channel.send(gif_url)

    if msg == '$anime-cry':
        gif_url = anime_cry_gif()
        await message.channel.send(gif_url)


# keeps on pinging the bot and keeps it running 24/7
keep_alive()
discord_client.run(DB_Token)
