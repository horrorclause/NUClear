# NUClear

Written in python3
Allows you to cycle through lists of domains at random in Chrome using selenium and chromedriver

Will cycle through domains at random from randomly selected listed of domains that you have designated in your domain list folder.

-- Make sure you check which version of Chrome you are using and download the correct chromedriver--

Download the chromedriver here: https://chromedriver.chromium.org/downloads

point the "browser" vairable to the location of the driver:
(ex. browser = webdriver.Chrome(r"C:\Users\bob\Desktop\Folder\chromedriver_win32\chromedriver.exe", options=options))

Point the "listsDir" variable to the folder containing your various lists.
(ex. listsDir = "C:\\Users\\bob\\Desktop\\folder\\") *escape the backslashes

