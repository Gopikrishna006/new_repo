from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://omayo.blogspot.com/")
# driver.maximize_window()
#
# driver.find_element("xpath","//button[.='Check this']").click()
#
# driver.find_element("id","dte").click()

driver.get("https://www.bigbasket.com/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath","//button[.='Login/ Sign Up']").click()
sleep(2)
driver.find_element("xpath","//input[@placeholder='Enter Phone number/ Email Id']").send_keys("7680030825")
sleep(2)
driver.find_element("xpath","//button[.='Continue']").click()
sleep(4)

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(10)
# driver.get("https://demoapps.qspiders.com/ui/progress/element?sublist=2")
#
# # sleep(2)
# driver.maximize_window()
# # sleep(2)
#
# driver.find_element("xpath","//input[@placeholder='Enter time in seconds']").send_keys("4")
# # sleep(2)
#
#
# element=driver.find_element("xpath","//button[.='Start']")
# element.click()
# wait=WebDriverWait(driver,10,poll_frequency=0.0003)
# percentage=wait.until(EC.visibility_of_element_located(("xpath","//span[//span[.='71%']]")))
#
# driver.find_element("xpath","//button[.='Pause']").click()
# sleep(3)
# driver.find_element("xpath","//select[contains(@class,'border-0 px-3 py-3')]").click()
# # sleep(3)