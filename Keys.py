from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
sleep(2)
driver.maximize_window()
sleep(2)
first=driver.find_element("id","input-firstname")
first.send_keys("krishna")
action=ActionChains(driver)
(action.send_keys("krishna").send_keys(Keys.TAB).send_keys("gopi").send_keys(Keys.TAB).send_keys("gopikrishnagopi098@gmail.com").send_keys(Keys.TAB).send_keys("7680030825").send_keys(Keys.TAB).send_keys("Krishna").send_keys(Keys.TAB).send_keys("Krishna").send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.SPACE).send_keys(Keys.ENTER).perform())
sleep(4)


# driver.get("https://demowebshop.tricentis.com/login")
#
# driver.maximize_window()
# sleep(2)
# links=driver.find_elements("xpath","//div[@class='column information']//a")
#
# sleep(2)
# actions=ActionChains(driver)
#
# for link in links:
#     link_text=link.text
#     element=driver.find_element('link text','link_text')
#     actions.KEYS_DOWN(Keys.CONTROL).click(element).KEYS_UP(Keys.CONTROL).perform()