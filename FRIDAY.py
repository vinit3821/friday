from threading import Timer
import PyQt5
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random 
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import pyjokes 
import pyautogui
import requests,json
from bs4 import BeautifulSoup
from time import sleep
import ctypes
import speedtest
import operator
from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTime, QTimer,Qt,QDate
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from FridayUI import Ui_FRIDAYUI




#text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#to wish
def wishme():
    hour = int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M:%p")
    if hour>=0 and hour<=12:
        speak(f"good morning,its{tt}")
    elif hour>12 and hour<18:
        speak(f"good afternoon,its{tt}")
    else:
        speak(f"good evening,its{tt}")
    speak("welcome back sir,all systems will be prepared in a few minutes...................................hello I am online mera naam friday hai mai apki k yaa madad kar sakti hu sir")            

#for news updates
def news():
    main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'

    main_page=requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today,s{day[i]} news is: {head[i]}")
    
class MainThread(QThread):
   def __init__(self): 
        super(MainThread,self).__init__()

   def run(self):
       while True:
          self.query=self.takecommand()
          if "wake up friday"in self.query:
             self.Taskexecution()
        
         
           

   def takecommand(self):
      r=sr.Recognizer()
      with sr.Microphone() as source:
          print("listening...")
          r.pause_threshold = 1
          audio = r.listen(source)
        
      try:
          print("recognizing...")
          self.query=r.recognize_google(audio, language='en-in')
          print(f"user said: {self.query}\n")

      except Exception as e:
          print(e)
          #speak("I dont get it please say that again") 
          return "none"
      self.query=self.query.lower()    
      return self.query

   def Taskexecution(self):
        wishme()
        print(pyautogui.__version__)
        while True:
        #if 1:   
           self.query= self.takecommand()

           #logic building for task
           if'sanju' in self.query:
               speak("hello master")
            
           elif 'open word' in self.query:
               speak("opening word")
               npath="C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
               os.startfile(npath)

           elif'open team'in self.query:
               speak("opening teams")
               tpath="C:\\Users\\lenovo\\AppData\\Local\\Microsoft\\Teams\\previous\\Teams.exe"
               os.startfile(tpath)    
        
           elif 'do you remember me' in self.query:
               speak("first tell me your name")
         
           elif 'vineet' in self.query:
               speak(f"Welcome {query} sir your are my creator how can i forget you\n")

           elif'mohit' in self.query:
               speak(f"hello {query} sir\n")
        
           elif'pinky' in self.query:
               speak("hello mummy")

           elif 'saroj' in self.query:
               speak("hello mummy")

           elif'babli' in self.query:
               speak("hello mummy")

           elif 'rahul' in self.query:
               speak(f"Welcome {self.query} sir you are my creator as well how are you \n")

           elif 'vicky' in self.query:
               speak(f"Welcome {self.query}bhaiya \n")

           elif 'who are you'in self.query or 'about yourself'in self.query:
               speak("i am an artificial intelligence based assistant program my name is friday,may i help you with something")         

           elif 'how are you' in self.query:
               speak("I am good sir how are you \n")

           elif 'kya hal' in self.query:
               speak("saab baadhaiyaa aappp baataoo sir \n")

           elif 'kaisi ho' in self.query:
               speak("saab baadhaiyaa aappp baataoo sir \n")        

           elif 'also good' in self.query:
               speak("thats great to hear from you sir\n") 

           elif'tell me the current time'in self.query:
               tt=time.strftime("%I:%M:%p")
               speak(f"the current time is{tt} ")       
        
           elif 'open camera' in self.query:
               cap=cv2.VideoCapture(0)
               while True:
                   ret, img =cap.read()
                   cv2.imshow('webcam',img)
                   k = cv2.waitKey(50)
                   if k==27:
                       break;
               cap.release()
               cv2.destroyAllWindows()

           elif 'play music' in self.query or'play some music'in self.query:
               speak("ok sir,playing music")
               music_dir="D:\\Music\\My Music"
               songs=os.listdir(music_dir)
               rd= random.choice(songs)
               os.startfile(os.path.join(music_dir, rd))

           elif 'ip address'in self.query:
               ip = get('https://api.ipify.org').text
               speak(f"your IP adress is {ip}\n ")

           elif'internet speed'in self.query:
               speak("sir please wait checking internet speed")
               st=speedtest.Speedtest()
               dl=st.download()
               up=st.upload()
               speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")


           elif 'wikipedia' in self.query:
               speak("searching wikipedia")
               query=query.replace("wikipedia","")
               results= wikipedia.summary(query,sentences=2)
               speak("According to wikipedia")
               speak(results)

           elif"hello"in self.query:
               speak("hello sir, may i help you with something")    

           elif 'open youtube'in self.query:
               speak("opening youtube sir")
               webbrowser.open("https://www.youtube.com/")

           elif 'search on youtube'in self.query:
               speak("sir what should i search on youtube")
               cm = self.takecommand()
               kit.playonyt(f"{cm}\n")    

           elif 'open google'in self.query:
               speak("sir what should i search on google")
               cm = self.takecommand().lower()
               webbrowser.open(f"{cm}")         

           elif 'open whatsapp'in self.query:
               speak("opening whatsapp")
               webbrowser.open("https://web.whatsapp.com/")

           elif'send message' in self.query:
               #speak("sir what you want to send")
               #time.sleep(1)
               #cm= takecommand().lower()
               kit.sendwhatmsg("+919871693695","hello",5,50)
               speak("message has been sent")
            
           elif'play song on youtube'in self.query:
               speak("sir what you want to play")
               cm= self.takecommand().lower()
               kit.playonyt(f"{cm}\n")

           elif'play music on youtube'in self.query:
               speak("sir what you want to play")
               cm= self.takecommand().lower()
               kit.playonyt(f"{cm}\n")

           elif'click'in self.query:
               speak("ok sir")
               pyautogui.click()

           elif'volume up' in self.query:
               speak("ok sir")
               pyautogui.press("volumeup")

           elif'volume down' in self.query:
               speak("ok sir")
               pyautogui.press("volumedown")

           elif'mute volume' in self.query:
               speak("ok sir")
               pyautogui.press("volumemute")            

           elif'sound sexy'in self.query:
               speak("Oh, oh, oh Aaah aah,  oh yeah baby oh yeah! aah aah you can do it yes yes fast fast oh my god mummy mummy ae mummy aaaaaah oh oh, oh, ahhh ahhh")        

           elif'no thanks'in self.query:
               speak("ok sir,as your wish")

           elif'bye'in self.query:
               speak("thanks for using me sir,have a good day")
               break

           elif'go to sleep'in self.query:
               speak("ok sir i am going to sleep you can call me anytime")
               break

           elif'you can sleep'in self.query:
               speak("ok sir i am going to sleep you can call me anytime!")
               break

           elif'thanks'in self.query or 'thank you'in self.query:
               speak("its my pleasure sir!")
               
            
           elif"that's all for now"in self.query:
               speak("ok sir")
               break

           elif"terminate yourself"in self.query:
               speak("thanks for using me sir have a nice day")
               sys.exit()

           elif'activate how to do mod'in self.query:
               from pywikihow import search_wikihow
               speak("how to do mode is activated please tell me what you want to know")
               how=self.takecommand()
               max_results=1
               how_to =search_wikihow(how,max_results)
               assert len(how_to) == 1
               how_to[0].print()
               speak(how_to[0].summary)    

           elif'do some calculation'in self.query or 'can you calculate'in self.query:
               r=sr.Recognizer()
               with sr.Microphone() as source:
                   speak("say what you want to calculate,")
                   print("listening...")
                   r.adjust_for_ambient_noise(source)
                   audio=r.listen(source)
               my_string=r.recognize_google(audio)
               print(my_string)
               def get_operator_fn(op):
                       return{
                           '+':operator.add,#plus
                           '-':operator.sub,#minus
                           '*':operator.mul,#multiply
                           'divided':operator.__truediv__,#divided
                           }[op]
               def eval_binary_expr(op1,oper,op2):
                   op1,op2=int(op1),int(op2)
                   return get_operator_fn(oper)(op1,op2)
               speak("your result is")
               speak(eval_binary_expr(*(my_string.split())))         

#to find my location 
           elif'where am i'in self.query or 'where we are' in self.query:
               speak("wait sir, let me check")
               try:
                   ipAdd = requests.get('https://api.ipify.org').text
                   print(ipAdd)
                   url ='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                   geo_requests = requests.get(url)
                   geo_data = geo_requests.json()
                   #print(geo_data)
                   city = geo_data['city']
                   #state = geo_data['state']
                   country = geo_data['country']
                   speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
               except Exception as e:
                   speak("sorry sir, Due to network issue i am not able to find where we are.")
                   pass

#to take screenshot
           elif'take screenshot'in self.query or 'take a screenshot'in self.query:
                   speak("sir,please tell me the name for this screenshot file")
                   name = self.takecommand().lower()
                   speak("please sir hold the screen for few seconds,i am taking screenshot")
                   time.sleep(1)
                   img = pyautogui.screenshot()
                   img.save(f"{name}.png")
                   speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")               

#to switch window
           elif'change the window'in self.query:
               speak("switching the window")
               pyautogui.keyDown('Alt')
               time.sleep(.2)
               pyautogui.press('Tab')
               time.sleep(.2)
               pyautogui.keyUp('Alt')
               speak("the window is switched")

#to tell news
           elif'tell me the news'in self.query:
               speak("please wait sir,fetching the latest news")
               news()

#to weather news
           elif'temperature'in self.query or 'weather' in self.query:
               speak("which place temperature you want to know")
               cm =self.takecommand().lower()
               search=(f" temperature in {cm}")
               url=f"https://www.google.com/search?q={search}"
               r=requests.get(url)
               data=BeautifulSoup(r.text,"html.parser")
               temp=data.find("div",class_="BNeawe").text
               speak("please wait sir,fetching the temperature info")
               speak(f"current {search} is {temp}")   

#to close my application
           elif'close word'in self.query:
               speak("okay sir,closing word")
               os.system("taskkill /f /im word.exe")

           elif'close chrome'in self.query:
               speak("ok sir,closing please wait a second")
               os.system("taskkill /f /im chrome.exe")    

#to set an alarm
           elif'set alarm' in self.query:
               speak("sir please tell me the time to set alarm. for example set alarm to 5:30 am")
               tt=self.takecommand()
               tt=tt.replace("set alarm to","")
               tt=tt.replace(".","")
               tt=tt.upper()
               import Myalarm
               Myalarm.alarm(tt)

#to find a joke
           elif'tell me a joke'in self.query or 'make me laugh'in self.query:
               speak("ok sir telling a joke here it is")
               joke=pyjokes.get_joke()
               speak(joke)

#to shut the system
           elif'shutdown the system'in self.query:
                   os.system("shutdown /s /t 5 ")

           elif'restart the system'in self.query:
               os.system("shutdown /r /t 5")

           elif'sleep the system'in self.query:
               os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")          
        #speak("sir,do you have any other work")

startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FRIDAYUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/project/FRIDAY/gifs/sFaoXq3.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/project/FRIDAY/gifs/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/project/FRIDAY/gifs/f16054ef24cddf2115e5524df9a54164.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/project/FRIDAY/gifs/98050d0e5e2ec6a063d514b7600a741c.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
   
    def showTime(self):
        current_time = QTime.currentTime()
        current_date= QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date=  current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
        


app = QApplication(sys.argv)
FRIDAY = Main()
FRIDAY.show()
exit(app.exec_())                 



