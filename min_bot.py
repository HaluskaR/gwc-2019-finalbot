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
@bot.command(name="yoda")
async def yoda(ctx, i):
	if "sad" in i or "bad" in i:
	    await ctx.send("https://www.reddit.com/r/FreshMemeTemplates/comments/e7tobr/baby_yoda_sad_reaching_star_wars_baby_yoda/")
	elif "good" in i or "fine" in i or "happy" in i:
	    await ctx.send("https://am22.akamaized.net/tms/cnt/uploads/2019/12/Baby-Yoda-With-His-Little-Cup-Is-All-of-Us.jpeg")
	elif "great" in i or "awesome" in i or "sweet" in i:
	    await ctx.send("https://i.kym-cdn.com/photos/images/original/001/691/226/dae.jpg")
	elif "worried" in i or "scared" in i:
	    await ctx.send("https://specials-images.forbesimg.com/imageserve/5dd93cc4ea103f0006532afb/960x0.jpg?fit=scale")
	else:
	    pass

with open("secret.txt","r") as secret_file:
    bot.run(secret_file.readline()[:-1])

