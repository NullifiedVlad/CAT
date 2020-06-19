import os
import shutil
os.system('pyinstaller -w -F -i "media\\icon.ico" CAT.py')
os.remove('CAT.spec')
try:

    with open(f'dist/CAT.exe', 'rb') as f:
        data = f.read()

    with open('CAT.exe', 'wb')as f:
        f.write(data)

        print('Компиляция успешно завершена!')
except Exception as e:
    print(e)
shutil.rmtree('build')
shutil.rmtree('dist')
