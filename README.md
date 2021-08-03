# NUClear

Written in python3

Allows you to cycle through lists of domains at random in Chrome using selenium and chromedriver
---------------------------------------------------------------------------------------------------------------------------

***Requires the selenium module for python3***
---------------------------------------------------------------------------------------------------------------------------



>> Make sure you check which version of Chrome you are using and download the correct chromedriver <<

Download the chromedriver: https://chromedriver.chromium.org/downloads


Windows
---------------------------------------------------------------------------------------------------------------------------

[+] Point the "browser" variable to the location of the driver:


**(ex. browser = webdriver.Chrome(r"C:\Users\bob\Desktop\Folder\chromedriver_win32\chromedriver.exe", options=options))**




[+] Point the "listsDir" variable to the folder containing your various lists.


**(ex. listsDir = "C:\\\Users\\\bob\\\Desktop\\\folder\\\\") escape the backslashes for use in Windows**

---------------------------------------------------------------------------------------------------------------------------

_Exceptions will be raised when timeouts occur because of killed traffic. The script will continue on._




For the Raspyberry PI 2/3/4 & Linux & Mac
---------------------------------------------------------------------------------------------------------------------------

**splitDirectory = file.name.split("\\") # For Linux or RPi change to "/" **


[+] The Selenium module needs to be installed for Python 3. Python 3 Should be installed by default on the RPi 3/4 so install selenium like so:

**"$pip3 install selenium"**



[+] Ensure that chromedriver for the Chromium browser is installed:

**"$sudo apt install chromium-chromedriver"**



[+] The "browser" variable should be set as such for headless:


**browser = webdriver.Chrome(r"/usr/lib/chromium-browser/chromedriver", options=options)**


[+] If using on a RPI and a sessionid failure exception is getting raised, clear the cache of the pi:

**sudo apt-get clean**


For FedoraOS & Fedora Server
---------------------------------------------------------------------------------------------------------------------------

$dnf upgrade

$dnf install chromium

$pip3 install selenium

chmod 755 /usr/bin/chromedriver

