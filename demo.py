# from time import sleep
#
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
#
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
#
# driver=webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(10)
# driver.get("https://testautomationpractice.blogspot.com/")
#
# driver.maximize_window()
# # sleep(2)
# driver.find_element("xpath","//input[@id='name']").send_keys('Krishna')
# # sleep()
# driver.find_element("xpath","//input[@id='email']").send_keys('gopikrishnagopi098@gmail.com')
#
# driver.find_element('id','phone').send_keys("7680030835")
#
# driver.find_element("id","textarea").send_keys('21 st street')
#
# driver.find_element("id","male").click()
#
# driver.find_element("id","wednesday").click()
#
# #drop down
# ---------------
# element=driver.find_element("xpath","//select[@class='form-control']")
# drop=Select(element)
#
# # drop.select_by_value('usa')
# # sleep(2)
#
# drop.select_by_visible_text("Canada")
# sleep(2)

# drop.select_by_index(2)
# sleep(2)

# count num of options
# print(len(drop.options))

# capture all the options
# all_options=drop.options
# list=[]
# for option in all_options:
#     print(option.text)

# el1=driver.find_element("xpath","//select[contains(@id,'colors')]")
# drop1=Select(el1)
# drop1.select_by_index(4)
# sleep(2)

# synchronization -Wait
#-------------------------
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(10)
# driver.get("https://demoapps.qspiders.com/ui/progress/disappear?sublist=3")
#
# driver.maximize_window()
# driver.find_element("xpath","//input[@placeholder='Enter time in seconds']").send_keys('4')
#
# driver.find_element("xpath","//button[.='Start']").click()
# wait=WebDriverWait(driver,10,poll_frequency=0.0005)
# per=wait.until(EC.visibility_of_element_located(("xpath","//span[.='77%']")))
#
# driver.find_element("xpath","//button[.='Pause']").click()
# sleep(3)