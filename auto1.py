# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_experimental_option("detch",True)
# driver = WebDriver(chrome_options)
#
# driver.get("https://www.google.com/")
# driver.close()

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.set_window_size(width=800,height=850)
sleep(4)
driver.find_element(by=By.ID,value='name').send_keys("krishna")
sleep(3)
driver.find_element(by=By.ID,value='email').send_keys("gopikrishnagopi098@gmail.com")
sleep(3)