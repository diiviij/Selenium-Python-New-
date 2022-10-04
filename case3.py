import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import time

s=Service('C:\Program Files (x86)\geckodriver-v0.31.0-win64\geckodriver.exe')
browser = webdriver.Firefox(service=s)
def timmer5():
    time.sleep(5)

browser.get("https://www.instagram.com/")
timmer5()

username = browser.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
username.send_keys('bottestdivij') #Enter Your Username 

password = browser.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
password.send_keys('Iambaba89') #Enter your password

login = browser.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')
login.click()
timmer5()

followers = browser.get("https://www.instagram.com/diiviij") #This is my Instagram Username
timmer5()
dmi = browser.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div')
dmi.click()
timmer5()
textbot = browser.find_element("xpath",'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
textbot.send_keys('Hi..how are you ??..Its a Bot generated text..please ignore it.')
timmer5()

sendtext= browser_find_elemenrt("xpath",'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
sendtext.click()
timmer5()

browser.quit()