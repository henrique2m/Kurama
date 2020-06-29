# coding= utf-8
import os

class Workspace:
    def openProgram(self, command=''):

        command.upper()

        try:
            if command == 'VSCODE':
                os.startfile(r"C:\Users\Henrique\AppData\Local\Programs\Microsoft VS Code\Code.exe")
                
        except Exception as error:
            raise error

