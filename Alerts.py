# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(10)
# driver.get("https://app.vwo.com/#/login")
# driver.maximize_window()
# driver.find_element("id","login-username").send_keys("gopikrishnagopi12#@gmail.com")


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
sleep(2)
# driver.find_element("xpath","//button[.='Click for JS Confirm']").click()
# sleep(3)
# alert=driver.switch_to.alert
# print(alert.text)
# alert.accept()
#
# sleep(3)

# driver.find_element("xpath","//button[.='Click for JS Confirm']").click()
# sleep(2)
# alert=driver.switch_to.alert
# print(alert.text)
# alert.dismiss()
# sleep(2)

driver.find_element("xpath","//button[.='Click for JS Prompt']").click()
sleep(2)
alert=driver.switch_to.alert
alert.send_keys("krishna")
sleep(2)
alert.accept()

sleep(2)