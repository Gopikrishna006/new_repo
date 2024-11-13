from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(8)
driver.get("file:///C:/Users/acer/Downloads/demo%20(1).html")
driver.maximize_window()

cal=driver.find_elements("xpath","//table[@name='customers']//tr//td[3]")


col4=driver.find_elements("xpath","//table[@name='customers']//tr//td[4]")

col3=[]
for col in cal:
    coll=col.text
    col3.append(coll)
print(col3)


row=[]
for cat in col4:
    row.append(cat.text)
print(row)
sleep(1)

# result=dict(zip(col3,row))
# print(result)
# sleep(2)
# sort_key=sorted(col3)
# sort_val=sorted(row)
# res=dict(zip(sort_key,sort_val))
# print(res)
# sleep(2)


output={}
for name in col3:
    percent=driver.find_element("xpath",f"//table[@name='customers']//tr//td[.='{name}']/..//td[4]").text
    if percent not in output:
        output[percent]=name
print(output)
sleep(2)