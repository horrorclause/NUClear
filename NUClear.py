#!/usr/bin/python3
import glob
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''

A script that will cycle through domains at random pulled from 
randomly selected lists of domains that you have designated in your 
domain list folder.

'''


# Put the path to the folder containing your lists of domains
listsDir = "PATH TO FOLDER CONTAINING LISTS"

# Chromedriver options -- Comment out the options if you dont want it headless.
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('log-level=3')  # Only output fatal errors

# Chrome webdriver for Selenium
browser = webdriver.Chrome(r"PATH TO CHROME DRIVER ->chromedriver.exe",
                           options=options)


# Enumerates all domain lists in specified directory, and randomly selects one
def fileDir():

    fileList = []

    for filepath in glob.iglob(listsDir+"*.txt"):
        fileList.append(filepath)

    randoFile = random.randint(0, len(fileList)-1)

    fullPath = fileList[randoFile]
    #splitPath = fullPath.split("\\")
    #listName = splitPath[-1]

    return fullPath


print('[+]===== BEGINNING HEADLESS =====[+]')

while True:

    try:
        # Pulls random domain from randomly selected list
        file = open(fileDir(), "r")
        pulledFile = file.readlines()
        splitDirectory = file.name.split("\\") # For Linux or RPI change to "/"
        domain = pulledFile[random.randint(0, len(pulledFile)-1)].strip()
        listName = splitDirectory[-1]

        print("[+] -- The domain is: "+domain)
        print("[+] -- Acquired from list: "+listName)

        # Selenium code to open browser with the listed domain
        page = browser.get("https://" + domain)

        browser.set_page_load_timeout(2) # Chromedriver will wait 8 seconds for page to load and then move on.

    except Exception as e:

        print("Exception raised")
        #print(e)
        pass





