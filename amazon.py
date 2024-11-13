from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)



# switch=driver.find_element("xpath","//div[@class='Header___StyledQuickSearch2-sc-19kl9m3-0 gzbZOD']//input[@type='text']")
# switch.send_keys("Apple")
# sleep(2)
# driver.find_element("xpath","//header[@style='opacity: 1;']//input[@type='text']").send_keys("Apple")
# sleep(2)
# driver.find_element("xpath","//span[text()='₹350']/../..//button").click()
# sleep(2)

driver.find_element("xpath","//input[@id='twotabsearchtextbox']").send_keys("shoes")
sleep(2)
driver.find_element("xpath","//input[@value='Go']").click()
sleep(2)

reviews=driver.find_elements("xpath","//span[@class='a-size-base s-underline-text']")
sleep(2)
list=[]
for review in reviews:
    list.append(review.text)
print(f'Highest reviews of shoes is : {max(list)}')
sleep(2)
driver.find_element("xpath","//span[.='99,848']").click()
sleep(5)
driver.find_element(("xpath","//input[@value='Add to Cart']")).click()
sleep(5)


# driver.find_element("css selector","""span[class="a-size-base-plus a-color-base a-text-normal"]""").click()
# sleep(4)