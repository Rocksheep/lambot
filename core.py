import discord
import dankmeme


help_message = '''```
+-------------------- Lambot Help --------------------+
[+] !slap (user): Slaps the named user
[+] !help: Shows all available command
[+] !dankmeme: Shows the dankest of maymays
+-----------------------------------------------------+
```'''

def command_help(client, said_words, message):
	yield from client.send_message(message.channel, help_message)

def command_slap(client, said_words, message):
	target = said_words[1]
	if target.lower() in masters:
		yield from client.send_message(message.channel, "If I do that he will scramble all my nibbles :(")
	else:
		yield from client.send_message(message.channel, "slapped {} with a massive pink dildo".format(target))

def command_dankmeme(client, said_words, message):
	meme_link = dankmeme.get_random_dank_meme()
	yield from client.send_message(message.channel, "Check this dank maymay: {}".format(meme_link))

masters = ['@rocksheep', 'rocksheep']
commands = {'!help': command_help, '!slap': command_slap, '!dankmeme': command_dankmeme}