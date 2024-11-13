from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(8)
# driver.get("https://www.w3schools.com/js/")
# driver.maximize_window()
#
# driver.find_element("xpath","//a[.='Try it Yourself »']").click()
#
# parent=driver.current_window_handle
# all_windows=driver.window_handles
#
# for handle in all_windows:
#     if handle != parent:
#         driver.switch_to.window(handle)
# sleep(2)
#
# frame=driver.find_element("xpath","//iframe[@id='iframeResult']")
# driver.switch_to.frame(frame)
# sleep(2)
# driver.find_element("xpath","//button[@type='button']").click()
# sleep(3)
#
# driver.get("https://www.w3schools.com/jsref/met_win_alert.asp")
#
# driver.maximize_window()
# driver.find_element("//div[@id='main']//div[@class='w3-example']//a[@class='w3-btn']")


