"""
Join to our telegram channel https://t.me/CAT_discord_dev
Jo to our telegram group https://t.me/catchatdev
Made by NullifiedVlad 2020
"""
import os
import sys
import config
from colorama import Fore
import shutil

print('''
   █████████    █████████   ███████████                                                 ███  ████                    
  ███░░░░░███  ███░░░░░███ ░█░░░███░░░█                                                ░░░  ░░███                    
 ███     ░░░  ░███    ░███ ░   ░███  ░      ██████   ██████  █████████████   ████████  ████  ░███   ██████  ████████ 
░███          ░███████████     ░███        ███░░███ ███░░███░░███░░███░░███ ░░███░░███░░███  ░███  ███░░███░░███░░███
░███          ░███░░░░░███     ░███       ░███ ░░░ ░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███  ░███ ░███████  ░███ ░░░ 
░░███     ███ ░███    ░███     ░███       ░███  ███░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███  ░███ ░███░░░   ░███     
 ░░█████████  █████   █████    █████      ░░██████ ░░██████  █████░███ █████ ░███████  █████ █████░░██████  █████    
  ░░░░░░░░░  ░░░░░   ░░░░░    ░░░░░        ░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░███░░░  ░░░░░ ░░░░░  ░░░░░░  ░░░░░     
                                                                             ░███                                    
                                                                             █████                                   
                                                                            ░░░░░ ''')
print(f'''{Fore.WHITE}Токен бота: {Fore.BLUE} {config.token}
{Fore.WHITE}Айди канала: {Fore.BLUE}{config.channel}''')

isAnswer = True

while isAnswer:
    answer = input(Fore.GREEN+'Если у вас Windows введите 1, если линукс введите 0: ')
    if int(answer) == 1:
        file = 'CAT.exe'
        isAnswer = False

    elif int(answer) == 0:
        file = 'CAT'
        isAnswer = False
    else:
        pass


if config.token == '':

    print(Fore.RED + 'Вы не вставили свой токен!')
    sys.exit()

elif config.channel == 228:

    print(Fore.RED + 'Вы не вставили айди канала куда должно отпровляться сообщение!')
    sys.exit()

else:

    os.system('pyinstaller -w -F CAT.py')
    os.remove('CAT.spec')
    shutil.rmtree('build')
    try:
        f = open(f'dist/{file}', 'rb')
        data = f.read()
        f.close()

        f = open(file, 'wb')
        f.write(data)
        f.close()

        shutil.rmtree('dist')
        print(Fore.GREEN+'Компиляция успешно завершена!')
    except FileNotFoundError:
        print(f'''{Fore.RED} Ошибка я не смог найти {file} , наверное вы изменили название файла CAT.py 
на другой или же вы выбрали не тот мод для компиляции!''')
        shutil.rmtree('dist')
