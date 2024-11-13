from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(8)
driver.get("https://www.instagram.com/")
driver.maximize_window()

parent_tab=driver.current_window_handle
print(parent_tab)
driver.find_element("link text","About").click()
all_handles=driver.window_handles
print(all_handles)

driver.switch_to.window(all_handles[1])

driver.find_element("link text","Log in").click()
all_handles=driver.window_handles


driver.switch_to.window(all_handles[2])
print(all_handles)
driver.find_element("xpath","//input[@name='username']").send_keys("krishna")

sleep(3)