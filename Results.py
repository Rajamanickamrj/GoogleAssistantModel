from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import speech_recognition as sr
import pyaudio
import os
import time
import pyttsx3
   
def get_results(search_terms):
   options = webdriver.ChromeOptions()
   #Hide Web Browser only use background process 
   options.add_argument('--headless')
   #Path for chromedriver.exe
   driver = webdriver.Chrome(executable_path=r'C:\Users\manic\Desktop\Python Program\chromedriver.exe', options=options)
   #Website link which was open for search 
   driver.get('https://www.google.com/')
   #Find search box for insert the query
   inputEles=driver.find_elements_by_css_selector('input[name=q]')
   for inputEle in inputEles :
      inputEle.send_keys(search_terms)
      inputEle.submit()
      try:
         #Metion the XPath for where they fetch the answer in search webpage
         text = driver.find_element_by_xpath("//*[@id=\"kp-wp-tab-overview\"]/div[1]/div/div/div/div[1]/div/div/div/div").text
      except:
         text = "Sorry could not find anything"
   time.sleep(5)
   driver.close()
   return text

#Program Start here     
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Ask Question : ")
    #Record your voice for 5 sec
    audio = r.record(source,duration=5)
    print("Recognizing your voice...")
    try:
       #Convert voice to text
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
    try:
       #Get the Web Search Results form get_results method
        stext=get_results(text)
        print(stext)
        #Initialize text to speach 
        engine = pyttsx3.init()
        #Data for text to Speach
        engine.say(stext)
        engine.runAndWait()
    except:
        print("Text to Speach Error")
