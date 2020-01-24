import random

import discord
from discord.ext import commands

screeches = ["AAAAAAAA", "OH NO OH NO", "HHOOOOAAAOAOAA", "EEEEEEEEAA", "YAAAAARGH", "OH GOSH OH GEEZ OH MAN", "OH FRICK OH HECK", "AAAA", "AAAAAAAAAAAAA", "[nonsensical shrieking]", "[high-pitched yelling]", "[upset walrus noise]", "[wilhelm scream]", "SCREEEEEEEE", "OH MAN OOOOOH MAAAAAN", "SNAKE? SNAAAAAKE!?", "YOOOOAAA", "[shrill ululation]", "YEEEEEEEBRBRBBRBRBRB"]

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        if random.randint(1, 10) == 5:
            await message.channel.send("***{}***".format(random.choice(screeches)))
    await bot.process_commands(message) 

@bot.command(name="roll")
async def roll(ctx, number=20):
    """Roll an unmodified die, d20 by default."""
    if number < 1:
        await ctx.send("Number must be greater than 1.")
        return
    await ctx.send("{res}\n(Rolled {num}, got {res})".format(num=number,
                                                             res=random.randint(1, number)))

@bot.command(name="swear")
async def swear (ctx, prompt):
	sCount = 0
	aCount = 0

	if "s" in prompt:
	  if "h" in prompt:
		if "i" in prompt:
		  if "t" in prompt:
			await ctx.send("shit")
	if "a" in prompt:
	  if "s" in prompt:
		for letter in prompt:
		  if letter is 's':
			sCount +=1
		if sCount >= 2:
		  await ctx.send("ass")
	if "b" in prompt:
	  if "i" in prompt:
		if "t" in prompt:
		  if "c" in prompt:
			if "h" in prompt:
			  await ctx.send("bitch")
	  if "a" in prompt:
		for letter in prompt:
		  if letter is 'a':
			aCount +=1
		if "s" in prompt:
		  if "t" in prompt:
			if aCount >= 2:
			  if "r" in prompt:
				if "d" in prompt:
				  await ctx.send("bastard")
	if "f" in prompt:
	  if "u" in prompt:
		if "c" in prompt:
		  if "k" in prompt:
			await ctx.send("fuck")
	else:
	  await ctx.send("finished")

with open("secret.txt","r") as secret_file:
    bot.run(secret_file.readline()[:-1])
