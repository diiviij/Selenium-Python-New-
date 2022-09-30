import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import time

s=Service('C:\Program Files (x86)\geckodriver-v0.31.0-win64\geckodriver.exe')
browser = webdriver.Firefox(service=s)
browser.get("https://www.instagram.com/")
time.sleep(5)

username = browser.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
username.send_keys('') #Enter Your Username 

password = browser.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
password.send_keys('') #Enter your password

login = browser.find_element("xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')
login.click()
time.sleep(10)

followers = browser.get("https://www.instagram.com/diiviij/followers/") #This is my Instagram Username


followerslist = browser.find_element("xpath", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div/span/a/span/div')
followersname = browser.find_element("innerHTML", '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div/span/a/span/div') 

#The above code lines will show you the list of my followers 



browser.quit()