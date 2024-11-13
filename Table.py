from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(8)
driver.get("https://demoapps.qspiders.com/ui/table?scenario=1")
driver.maximize_window()

ratings=driver.find_elements("xpath","//table//tbody//tr//td[2]")
rate=[]
for rating in ratings:
    rate.append(rating.text)
print(rate)
sleep(2)
total={}
for item in rate:
    if  item>='3':
       price=driver.find_element("xpath",f"//table//tbody//tr//td[.='{item}']/../td[4]").text
       if item not in total:
           total[item]=price
print(total)
sleep(2)


ratings=driver.find_elements("xpath","//table//tbody//tr//td[1]")
cmd=[]
for rate in ratings:
    cmd.append(float(rate.text.split()[0]))
print(cmd)
sleep(2)
result={}
for cd in cmd:
    res=driver.find_element("xpath",f"//table//tr//td[.='{cd} Star']/../th").text
    if res not in result:
        result[cd]=res
print(result)

sleep(2)

driver.find_element("partial link text","Dynamic Web Table").click()
sleep(3)