import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import time

s=Service('C:\Program Files (x86)\geckodriver-v0.31.0-win64\geckodriver.exe')
browser = webdriver.Firefox(service=s)
browser.get("https://google.com")
time.sleep(5)
# browser.get("https://www.geeksforgeeks.org/")
 
# # get element
# element = driver.find_element_by_xpath("//form[input/@name ='search']")
searchbar = browser.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchbar.send_keys('hello')
time.sleep(5)

browser.quit()