from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import select
from time import sleep


from selenium.webdriver.common.by import By

serv_obj =Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("file:///C:/Users/acer/Downloads/demo%20(1).html")
driver.maximize_window()
sleep(3)
down=driver.find_element("xpath","//select[@id='multiple_cars']")
# down.click()
s1=select(down)
sleep(2)
s1.select_by_index(2)
sleep(2)
s1.select_by_value("value='bmw'")
sleep(2)
# check_box=driver.find_element('name','download')
# check_box.click()
# sleep(3)
# link=driver.find_element('link text','Download')
# link.click()
# sleep(3)
# partial_link=driver.find_element('partial link text','100')
# partial_link.click()
# sleep(3)
# driver.find_element('id','firstname').send_keys('Gopi')
# sleep(3)