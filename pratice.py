from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(8)
# driver.get("file:///C:/Users/acer/Downloads/demo%20(1).html")
#
# tables=driver.find_elements("xpath",'//input[@type="text"]')
#
#
# list1=['krishna','prasad','mahesh','sai','prasanth','kala','ola','arey','python']
#
# index=0
# for table in tables:
#     if index<len(list1):
#          table.send_keys(list1[index])
#          index+=1
#          sleep(2)
driver.implicitly_wait(10)
driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
columns=driver.find_elements("xpath","//div[@class='footer']//a")
actions=ActionChains(driver)
index=0
for column in columns:
    if index%2!=0:
        actions.key_down(Keys.CONTROL).click(column).perform()
    index+=1
    sleep(2)
