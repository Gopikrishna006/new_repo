from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(8)
driver.get("https://demoapps.qspiders.com/ui/fileUpload?sublist=0")

driver.maximize_window()
driver.find_element("id","fileInput").send_keys("D://matlab//matlab 1.pdf")
sleep(2)