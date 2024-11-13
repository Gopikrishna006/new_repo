
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://demoapps.qspiders.com/ui/table")
# driver.maximize_window()
# sleep(1)
# texts=driver.find_elements("xpath","//table[@class='w-full text-sm text-left text-gray-500 ']//td")
# for i in texts:
#     print(i.text)
#     sleep(1)
#
# sleep(2)

driver.get("https://www.goibibo.com/flights/?utm_source=google&utm_medium=cpc&utm_campaign=DF-Brand-EM&utm_adgroup=Only%20Goibibo&utm_term=!SEM!DF!G!Brand!RSA!108599293!6504095653!617695092667!e!goibibo!c!&gad_source=1&gclid=Cj0KCQjw5ea1BhC6ARIsAEOG5pwJ7xCoyzGIEBX8uTYkwHQpT7IHhhgsPInw4jiTmvatE19msgzP1VcaAqkuEALw_wcB")
