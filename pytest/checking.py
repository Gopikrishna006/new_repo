from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

# serv=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=WebDriver()

driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
sleep(2)