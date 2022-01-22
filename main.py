"""


"""
import discord
import logging
import key as ky
from discord.ext import commands as cmds

# Variables
client = discord.Client()
bot = cmds.Bot(command_prefix='.')
logger = logging.getLogger('discord')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# EVENTOS
logger.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# Bot en funcionamiento (consola)
@client.event
async def on_ready():
    print('Bot {0.user} en funcionamiento'.format(client))


@bot.command()
async def hola(ctx):
    await ctx.reply('Hola!')
    
# Arranque
client.run(ky.Const_Key_cimabot)
# bot.run(ky.Const_Key_cimabot)


