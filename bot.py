# bot.py
import os
import discord
import asyncio
import requests
from discord.ext import commands
from dotenv import load_dotenv
from random import randrange


random_person = [
	'Къв си ти бе?',
	'Я некъв бушон влезе!',
	'На Сентропе или на Малдивите си?',
	'Извинете, вие ли духате за без пари?'
]

kukata = [
	'Извинете, вие ли духате за без пари?'
]

def rand_welcome():
	return random_person[randrange(0,len(random_person))]

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_member_join(member):
	if member.name == 'ninoo5':
		await member.send(f'Welcome fatso/shishi !!!')
		print(f'Message send to {member.name}')
	elif member.name == 'LizzardRider':
		await member.send(f'Welcome lazare!')
		print(f'Message send to {member.name}')
	elif member.name == 'Torbjørn':
		await member.send(f'Welcome Bonjorny!')
		print(f'Message send to {member.name}')
	elif member.name == 'Onatie':
		await member.send(f'Само няма ми се депресираш...Капиш?')
		print(f'Message send to {member.name}')
	else:
		await member.send(f'{rand_welcome()}')
		print(f'Message send to {member.name}')

@bot.event
async def on_raw_member_remove(ctx):
	await ctx.send(f'Аре баста {ctx.user.name}')

@bot.event
async def on_ready():
	print('Bot loaded!')
	print(f'Name: {bot.user.name}')
	print(f'ID: {bot.user.id}')

@bot.command()
async def test(ctx):
	await ctx.send('Tested!')

@bot.command()
async def kaji_neshto(ctx):
	async with ctx.typing():
		await asyncio.sleep(randrange(1,2))
	await ctx.send(kukata[randrange(0, len(kukata))])

weather_url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

wather_querystring = {"lat":"42.698334","lon":"23.319941"}

weather_headers = {
	"X-RapidAPI-Key": "1a38b19767mshd42625c0a47ee96p1c4296jsna6542bf09238",
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

@bot.command()
async def vremeto(ctx):
	data = requests.get(weather_url, headers=weather_headers, params=wather_querystring).json()
	async with ctx.typing():
		await asyncio.sleep(randrange(1,2))
	await ctx.send(f"It's {data['data'][0]['weather']['description']} bro и глей кво става {data['data'][0]['temp']}°C баси майката")

async def load_ext():
	for f in os.listdir('./cogs'):
		if f.endswith('.py'):
			await bot.load_extension(f'cogs.{f[:-3]}')

async def main():
	async with bot:
		await load_ext()
		await bot.start(TOKEN)

asyncio.run(main())