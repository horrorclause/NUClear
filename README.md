# NUClear

Written in python3
Allows you to cycle through lists of domains at random in Chrome using selenium and chromedriver

*Requires the selenium module for python3*

Will cycle through domains at random from randomly selected lists of domains that you have designated in your domain list folder.

-- Make sure you check which version of Chrome you are using and download the correct chromedriver--

Download the chromedriver: https://chromedriver.chromium.org/downloads

point the "browser" variable to the location of the driver:
(ex. browser = webdriver.Chrome(r"C:\Users\bob\Desktop\Folder\chromedriver_win32\chromedriver.exe", options=options))

Point the "listsDir" variable to the folder containing your various lists.
(ex. listsDir = "C:\\Users\\bob\\Desktop\\folder\\") *escape the backslashes

Exceptions will be raised when timeouts occur because of killed traffic. The script will continue on.

If using on a RPI and a sessionid failure exception is getting raised, clear the cache of the pi:

sudo apt-get clean


**### For the Raspyberry PI 3/4**


The Selenium module needs to be installed for Python 3. Python 3 Should be installed by default on the RPi 3/4 so install selenium like so:

"$pip3 install selenium"

Ensure that chromedriver for the Chromium browser is installed:

"$sudo apt install chromium-chromedriver"


