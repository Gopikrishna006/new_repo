from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service




serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://docs.oracle.com/javase/8/docs/api/")

driver.maximize_window()
driver.switch_to.frame("classFrame")

print("Provides the classes necessary to create an applet and the classes an applet")

driver.switch_to.default_content()
sleep(2)

t3=driver.find_element("xpath","//frame[@name='packageFrame']")
driver.switch_to.frame(t3)
action=ActionChains(driver)

abstract_item=driver.find_element("xpath","//a[.='AbstractAction']")

action.key_down(Keys.CONTROL).click(abstract_item).key_up(Keys.CONTROL).perform()
sleep(3)


driver.switch_to.default_content()

content=driver.find_element("xpath","//frame[@name='packageListFrame']")
driver.switch_to.frame(content)
sleep(2)
applink=driver.find_element("xpath","//a[.='java.applet']")

action.key_down(Keys.CONTROL).click(applink).perform()

sleep(3)

# state Element Reference
# ------------------------

driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
driver.find_element("xpath","//input[@value='Search store']").send_keys("shoes")
