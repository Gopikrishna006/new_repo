from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
# driver.get("https://demoapps.qspiders.com/ui/datePick?sublist=0")
# driver.maximize_window()

# driver.find_element("xpath","//section[.='Date & Time Picker']").click()
# driver.find_element("xpath","//section[.='Date Picker']").click()
# txt_box=driver.find_element("xpath","//div[@class='react-datepicker__input-container']")
# txt_box.click()
# december=driver.find_element("xpath","//div[@class='react-datepicker__current-month']")
# nxt_button=driver.find_element("xpath","//button[@type='button'][2]")
#
# # for i in range(9):
# #     nxt_button.click()
# #     sleep(2)
#
# while december.text !='August 2025':
#     nxt_button.click()
#     sleep(1)
#
# driver.find_element("xpath","//div[@class='react-datepicker__month']//div[.='20']").click()
#
# sleep(3)

# driver.find_element("partial link text","Dropdown").click()
# sleep(3)
# driver.find_element("xpath","//input[@placeholder='Select A Date']").click()
# driver.find_element("xpath","//div[@class='react-datepicker__month-read-view']").click()
#
# driver.find_element("xpath","//div[.='Jun']").click()
#
# driver.find_element("xpath","//div[.='2024']").click()
#
# driver.find_element("xpath","//div[.='2023']").click()
#
# sleep(2)


# Time picker
# ------------
driver.get("https://demoapps.qspiders.com/ui/timePick?sublist=0")
driver.maximize_window()
# driver.find_element("xpath","//input[@placeholder='hh:mm aa']").click()
#
# actions=ActionChains(driver)
# actions.send_keys('22').send_keys('11').perform()
# sleep(2)

driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root')]").click()


# with keys
# -----------

# data=driver.find_element("xpath","//li[.='10']")
#
# data.send_keys(Keys.PAGE_DOWN)
# sleep(2)

# picker=driver.find_elements("xpath","//div[@role='group']//ul[1]//li")
#
# pause=driver.find_element("xpath","//li[.='11']")
# for pick in picker:
#     if pick.text=="11":
#         pause.click()
#         sleep(.5)
# sleep(2)

# scroll down
# ------------
# scroll_BY_amount()
# scroll_to_element()

