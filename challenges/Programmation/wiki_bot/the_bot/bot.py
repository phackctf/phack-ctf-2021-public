""""
Copyright © Krypton 2021 - https://github.com/kkrypt0nn
Description:
This is a template to create your own discord bot in python.

Version: 2.3
"""

import discord, asyncio, os, platform, sys
from discord.ext.commands import Bot
from discord.ext import commands
if not os.path.isfile("config.py"):
	sys.exit("'config.py' not found! Please add it and try again.")
else:
	import config

from challenge import *
import datetime

"""
Setup bot intents (events restrictions)
For more information about intents, please go to the following websites:
https://discordpy.readthedocs.io/en/latest/intents.html
https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents


Default Intents:
intents.messages = True
intents.reactions = True
intents.guilds = True
intents.emojis = True
intents.bans = True
intents.guild_typing = False
intents.typing = False
intents.dm_messages = False
intents.dm_reactions = False
intents.dm_typing = False
intents.guild_messages = True
intents.guild_reactions = True
intents.integrations = True
intents.invites = True
intents.voice_states = False
intents.webhooks = False

Privileged Intents (Needs to be enabled on dev page):
intents.presences = True
intents.members = True
"""

intents = discord.Intents.default()

bot = Bot(command_prefix=config.BOT_PREFIX, intents=intents)

# The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
	bot.loop.create_task(status_task())
	print("--------------------------------------")
	print(f"Logged in as {bot.user.name}")
	print(f"Discord.py API version: {discord.__version__}")
	print(f"Python version: {platform.python_version()}")
	print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
	print("--------------------------------------")


# Setup the game status task of the bot
async def status_task():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="les équipes galérer."))


# The code in this event is executed every time someone sends a message, with or without the prefix
@bot.event
async def on_message(message):

	if message.author == bot.user or message.author.bot:
		return
	else:
		print(f"{datetime.datetime.now()} -- Got the message \"{message.content}\" from {message.author.name}")
		if message.author.name not in config.BLACKLIST:
		    if message.channel and message.channel.id == message.author.dm_channel.id: # dm only
			    if message.author.id not in USERS:
			        await message.author.send(f"🌺 Welcome new human 🌺\n\nYou're name is {message.author.name}? It sucks! 🤮 You should change it. Only my master's name sounds and looks great to me!\nLove you ❤️ <@!418022155062870017> ❤️")
			        await message.author.send("...")
			        await message.author.send("This being said...💬")
			        await message.author.send("Wanna play with me ? 🤾 ")

			        USERS[message.author.id] = User(message.author.id)
			        USERS[message.author.id].step = Step.WANNA_PLAY
			    else:
			        if USERS[message.author.id].step == Step.WANNA_PLAY:
			            if message.content in ("Y", "Yes", "yes", "Oui", "oui", "ok", "OK"):
			                await message.author.send("Okay, cool! Let's play!")
			                await message.author.send("Here are the 📏 rules 📏 : \nI will ask you some questions about famous people because I like stalking.\n\nGive me the good answer to all of them and I'll give you the precious flaggy text.\nOh, and you have only {} seconds to answer.\nGood luck.".format(str(DELAY)))
			                await message.author.send("Is that okay ?")
			                USERS[message.author.id].step = Step.INSTRUCTION
			            elif message.content in ("N", "No", "no", "Non", "non", "nope"):
			                await message.author.send("Ah, too bad!")
			                await message.author.send("See you later...! 🤼‍")
			                del USERS[message.author.id]
			            else:
			                await message.author.send("Huum? What?")

			        elif USERS[message.author.id].step == Step.INSTRUCTION:
			            if message.content in ("Y", "Yes", "yes", "Oui", "oui", "ok", "OK"):
			                await message.author.send("Let's go !")
			                USERS[message.author.id].step = Step.PLAYING
			                current_user = USERS[message.author.id]
			                current_user_question = QUESTIONS[current_user.questions[current_user.current_question]]
			                await message.author.send(f"**Question #{str(current_user.current_question + 1)}** : {current_user_question.label}")
			                USERS[message.author.id].asked_time = datetime.datetime.now()
			            elif message.content in ("N", "No", "no", "Non", "non", "nope"):
			                await message.author.send("Ah, too bad!")
			                await message.author.send("See you later...! 🤼‍")
			                del USERS[message.author.id]
			            else:
			                await message.author.send("Huum? What?")

			        elif USERS[message.author.id].step == Step.PLAYING:
			            current_user = USERS[message.author.id]
			            current_user_question = QUESTIONS[current_user.questions[current_user.current_question]]
			            time_to_answer = (datetime.datetime.now() - current_user.asked_time).total_seconds()
			            if time_to_answer > DELAY:
			                await message.author.send("Ohoh.\nThis is a late response.⏲️ Hurry up !\n(Challenge rebooting...)")
			                del USERS[message.author.id]
			                print(f"{datetime.datetime.now()} -- Time to answer the question by {message.author.name} : {str(time_to_answer)}sec")
			            elif message.content == current_user_question.answer:
			                await message.author.send("Well done ! <:logoPhackCTF_2coul_VioletVert2:806195671203446816>")
			                USERS[message.author.id].current_question += 1

			                if USERS[message.author.id].current_question >= len(QUESTIONS):
			                    USERS[message.author.id].step = Step.WIN
			                else:
			                    current_user = USERS[message.author.id]
			                    current_user_question = QUESTIONS[current_user.questions[current_user.current_question]]
			                    await message.author.send(f"**Question #{str(current_user.current_question + 1)}** : {current_user_question.label}")
			                    USERS[message.author.id].asked_time = datetime.datetime.now()
			            else:
			                await message.author.send("Arf.😫 No, this is wrong!\nI have to reset your game.\nBye!")
			                del USERS[message.author.id]

			        elif USERS[message.author.id].step != Step.WIN:
			            await message.author.send("I don't know what to do now.. 😆")

		    # else:
			#     await message.author.send("Please, send me a PM instead. ;)")

		    if message.author.id in USERS and USERS[message.author.id].step == Step.WIN:
			    await message.author.send(f"GG.🥒\n\nThe flag is **{FLAG}**.\nYou deserved it ! Enjoy the rest of the event.\n\nBye bye!\n🍻🍻")
			    await message.author.send("https://tenor.com/view/mission-impossible-we-got-this-you-got-this-aja-oh-yeah-gif-9140872")


		# else:
		# 	# Send a message to let the user know he's blacklisted
		# 	context = await bot.get_context(message)
		# 	embed = discord.Embed(
		# 		title="You're not authorized to send message here!",
		# 		description="Ask the owner to add you into the list if you think it's not normal.",
		# 		color=0xFF0000
		# 	)
		# 	await context.send(embed=embed)



if __name__ == "__main__":
	# Removes the default help command of discord.py to be able to create our custom help command.
    bot.remove_command("help")
	# Run the bot with the token
    bot.run(config.TOKEN)
