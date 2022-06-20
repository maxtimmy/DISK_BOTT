import discord
from discord.ext import commands
from random import choice
import os
import config

bot = commands.Bot(command_prefix=config.settings['prefix'], intents=discord.Intents.all())


@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
@commands.has_permissions(administrator=True)
async def сбор(ctx):
    for channel in ctx.guild.voice_channels:
        for member in channel.members:
            await member.move_to(ctx.author.voice.channel)


@bot.command()
async def greh(ctx, name: str,kol : int):
    await ctx.message.delete()
    o=[]
    for channel in ctx.guild.voice_channels:
        o.append(channel)
    for channel in ctx.guild.voice_channels:
        for member in channel.members:
            if str(member) == name:
                greshnik = member
                for j in range(kol):
                    for i in range(5):
                        await member.move_to(o[1])
                        await member.move_to(o[0])

    await greshnik.move_to(ctx.author.voice.channel)



bot.run(config.settings['token'])
