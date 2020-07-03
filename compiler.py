import os
import shutil
from tkinter import *

window = Tk()
window.resizable(width=False, height=False)
window.iconbitmap('media\\icon.ico')
window.geometry('300x200')
label = Label(text='COMPILER', font='Impact 50',
              fg='#ccc',
              bg='#6b6b6b')
label.place(x=0, y=80)
login = Label(text='Token', font='Impact 10',
              fg='#ccc',
              bg='#6b6b6b')
token = Entry(window,
              font='Arial 11',
              bg='#ccc',
              fg='#303030',
              show='*')
button = Button(window)
window['bg'] = '#6b6b6b'
window.title('CAT compiler')
login.pack()
token.pack()
window.mainloop()

"""os.system('pyinstaller -w -F -i "media\\icon.ico" CAT.py')
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
"""
