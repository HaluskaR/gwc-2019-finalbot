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

@bot.command(name="mandy")
async def mandy(ctx, triggerword=None):
    """Talk to Mandy!"""
    if triggerword is not None:
        await ctx.send("no")
			 
															 
with open("secret.txt","r") as secret_file:
    bot.run(secret_file.readline()[:-1])
