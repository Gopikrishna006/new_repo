from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(8)
driver.get("https://www.youtube.com/watch?v=nZiJTYiujUs&list=RDCLAK5uy_lyVnWI5JnuwKJiuE-n1x-Un0mj9WlEyZw&index=4")
driver.maximize_window()
wait=WebDriverWait(driver,80)
pause=wait.until(EC.visibility_of_element_located(("xpath","//button[@title='Play (k)']")))
pause.click()
sleep(3)