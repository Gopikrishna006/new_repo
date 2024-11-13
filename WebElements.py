from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

ser_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

# text box-register page
# -------------------------
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
driver.maximize_window()
driver.find_element("id","name").send_keys("krishna")
driver.find_element("name","email").send_keys("gopikrish@gmail.com")
driver.find_element("id","password").send_keys("password")
driver.find_element("xpath","//button[.='Register']").click()
sleep(2)
# driver.find_element("partial link text"," Login").click()
# sleep(2)
# login page with xpath
#-------------

driver.find_element("xpath","//input[@id='email']").send_keys("gopikrish@gmail.com")
driver.find_element("xpath","//input[@name='password']").send_keys("password")
driver.find_element("xpath","//button[.='Login']").click()
sleep(2)

# button-default click
# ----------------------

driver.find_element("xpath","//section[.='Button']").click()
driver.find_element("id","btn").click()
driver.find_element("xpath","//section[@class='px-4']/article[2]/button[2]").click()
driver.find_element("xpath","//button[@id='btn6']").click()
sleep(3)

# Right click
# -------------

driver.find_element("xpath","//a[.='Right Click']").click()
actions=ActionChains(driver)
right_click=driver.find_element("id","btn30")
sleep(2)
actions.context_click(right_click).perform()

driver.find_element("xpath","//div[.='Yes']").click()
sleep(3)

# double click
# --------------

driver.find_element("xpath","//a[.='Double Click']").click()
double_click=driver.find_element("id","btn20")
actions=ActionChains(driver)

actions.double_click(double_click).perform()
sleep(2)

# submit click
# --------------

driver.find_element("xpath","//a[.='Submit Click']").click()
driver.find_element("xpath","//input[@id='prob2']").click()
driver.find_element("id","btn41").click()
sleep(2)

# link text-defult
# -----------------

driver.find_element("xpath","//section[.='Link']").click()

contact=driver.find_element("xpath","//a[.='Contact Us']")

actions=ActionChains(driver)
actions.key_down(Keys.CONTROL).click(contact).key_up(Keys.CONTROL).perform()
sleep(3)
links=driver.find_elements("tag name","a")
# for link in links:
#     href=link.get_attribute("href")
#     if href:
#         print(href)

sleep(1)
for link in links:
    link=link.text
    print(link)
# sleep(1)
# for link in links:
#     print(f'{link}-->{driver.title}')

sleep(2)
count_links=len(links)
print(count_links)


# for link in links:
#     link.click()
# sleep(2)


# Drop Down
# ----------
driver.find_element("xpath","//section[.='Dropdown']").click()
sleep(3)
s1=driver.find_element("xpath","//select[@id='select1']")
s1.click()
driver.find_element("xpath","//input[@id='phone']").send_keys("7680030825")

select=driver.find_element("xpath","//select[@id='select2']")
sel=Select(select)
sel.select_by_index(1)

select1=driver.find_element("xpath",'//select[@id="select3"]')
sel1=Select(select1)
sel1.select_by_value(value="India")
select2=driver.find_element("xpath",'//select[@id="select5"]')
sel2=Select(select2)
sel2.select_by_visible_text("Andhra Pradesh")


# Date & Time date picker
# -----------------------
driver.find_element("xpath","//section[.='Date & Time Picker']").click()
driver.find_element("xpath","//section[.='Date Picker']").click()
driver.find_element("xpath","//input[@placeholder='Select A Date']").click()
# december=driver.find_element("xpath","December 2024")
december=driver.find_element("xpath","//span[.='Next Month']").click()
# chrome_options.add_experimental_options()
# driver=webdriver.Chrome(Options=chrome_opitons)
# while december.text !="December 2024":
#     december.click()
#     sleep(3)
sleep(3)




