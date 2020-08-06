from tkinter import *
import os
import shutil


class SettingsWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Information')
        self.geometry('400x200')
        self.resizable(0, 0)
        self['bg'] = '#303030'


class InfoWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Information')
        self.geometry('400x200')
        self.resizable(0, 0)
        self['bg'] = '#303030'


class MainWindow(Tk):
    """
        Основное окно программы.
        """

    def __init__(self, title: str, geometry: str, background: str):
        super().__init__()
        self.background = background
        self.title(title)
        self.geometry(geometry)
        self["bg"] = background
        self.resizable(0, 0)

    @staticmethod
    def compile():
        os.system('pyinstaller -w -F -i "media\\icon.ico" CAT.py')
        os.remove('CAT.spec')
        try:

            with open(f'dist/CAT.exe', 'rb') as f:
                data1 = f.read()

            with open('CAT.exe', 'wb')as f:
                f.write(data1)

        except Exception as x:
            print(x)
        shutil.rmtree('build')
        shutil.rmtree('dist')

    def run(self):
        Label(self, text='COMPILER', font='Impact 25', bg=self.background, fg='white').pack()

        # Download button
        Button(self, text='Compile',
               bd=0, font='Impact', bg='#424242',
               activebackground='#545454',
               activeforeground='white',
               command=self.compile).place(x=63, y=75, width=128)

        self.mainloop()


if __name__ == '__main__':
    MainWindow('CAT Compiler', '255x160', '#303030').run()
