from selenium import webdriver
from time import sleep
from random import randrange
import os
import re
import pandas as pd
import requests

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/your/path/chromedriver',chrome_options=chrome_options) #If you have Windows use .exe

USERNAME = "YOUR_USERNAME" #It must be changed
PASSWORD = "YOUR_PASSWORD" #It must be changed

print("Browser opened!")
driver.get("https://www.instagram.com/")
sleep(20)
print("Loading...")
driver.find_element_by_xpath("//input[@name=\"username\"]")\
    .send_keys(USERNAME) 
sleep(5)
driver.find_element_by_xpath("//input[@name=\"password\"]")\
    .send_keys(PASSWORD) 
sleep(5)
driver.find_element_by_xpath('//button[@type="submit"]')\
    .click()
sleep(20)
print("Logged!")
url = "https://www.instagram.com/{}"
driver.get(url.format(USERNAME))
sleep(20)
following = driver.find_element_by_partial_link_text("following")
following.click()
sleep(20)
unfollowed = 0
fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
sleep(10)
whiteList = ["curiosita_losapeviche_ita", "else"] #WHITE-LIST IF YOU WANT


for x in range(150): #YOU CAN CHANGE THIS VALUE
    try:
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody) #scroll
        sleep(1)
    except:
        print("All scrolled")
        break


users = driver.find_elements_by_class_name("FPmhX.notranslate._0imsa")

unfollowPath = "/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button"
iterator = 0

print("%d users" % len(users))
for user in users:
    jump = randrange(10)
    iterator += 1
    name = user.text
    if jump <= 7 and not name in whiteList: #unfollow
        user.find_element_by_xpath(unfollowPath.format(iterator)).click()
        sleep(5)
        driver.find_element_by_xpath('//button[text()="Unfollow"]').click()
        unfollowed += 1
        sleep(5)
        print("%d users unfollowed" % unfollowed)
        usernUnfollowed = "{} unfollowed"
        print(usernUnfollowed.format(name))
        wait = randrange(100, 300)
        sleep(wait)
    else: #not unfollowed
        toPrint = "Impossible unfollow: {}"
        print(toPrint.format(name))
