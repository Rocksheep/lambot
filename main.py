import discord
import asyncio
import core
import time
from configparser import ConfigParser

client = discord.Client()


@client.event
@asyncio.coroutine
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


@client.event
@asyncio.coroutine
def on_message(message):
	said_words = message.content.split(' ')
	command = said_words[0].lower()
	if command in core.commands:
		current_time = time.strftime("%Y-%m-%d %H:%M")
		print('{}: {} used the {} command'.format(current_time, message.author, command))
		yield from core.commands[command](client, said_words, message)

cfg = ConfigParser()
cfg.read('config.ini')
client.run(cfg.get('discord', 'username'), cfg.get('discord', 'password'))
