
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# serv=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
# driver=webdriver.Chrome(service=serv)
# driver.get("https://www.nopcommerce.com/en")
# driver.maximize_window()
# sleep(2)
#
#
# driver.find_element("xpath","html/body/div[7]/header[1]/nav[1]/ul[1]/li[1]/a").click()
# sleep(2)

# driver.find_element("xpath","//input[@name='username']").send_keys("admin")
# sleep(2)
# driver.find_element("xpath","//input[@type='password']").send_keys("admin123")
# sleep(2)
# driver.find_element("xpath","//button[@type='submit']").click()
# sleep(2)
#
# act_title=driver.title
# exp_title="OrangeHRM"
# if act_title==exp_title:
#       print("login test passed")
# else:
#       print("LOGIN TEST FAILED")
#
# sleep(2)

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
# driver.get("https://demoapps.qspiders.com/ui/frames?sublist=0")
#
# driver.maximize_window()
#
# file=driver.find_element("xpath","//iframe[@class='w-full h-96']")
# driver.switch_to.frame(file)
#
# driver.find_element("xpath","//input[@id='username']").send_keys("krishna")
#
# driver.find_element("xpath","//input[@id='password']").send_keys("krishna@098")
#
# driver.find_element("xpath","//button[.='Login']").click()
#
# driver.switch_to.default_content()
# driver.find_element("xpath","//select[@id='options']").click()
#
# driver.find_element("xpath","//option[.='API']").click()
# sleep(3)

# driver.get("https://demoapps.qspiders.com/ui/frames/nested?sublist=1")
#
# driver.maximize_window()
# sleep(2)
# iframe=driver.find_element("xpath","//iframe[@class='w-full h-96']")
# driver.switch_to.frame(iframe)
#
# nest=driver.find_element("xpath","//section[@class='main_form_container']//iframe")
# driver.switch_to.frame(nest)
#
# driver.find_element("id","email").send_keys("Admin@gmail.com")
#
# driver.find_element("id","password").send_keys("Admin@1234")
#
# driver.find_element("id","confirm-password").send_keys("Admin@1234")
#
# driver.find_element("xpath","//button[.='Sign Up']").click()
#
# sleep(4)


# driver.get("https://demoapps.qspiders.com/ui/frames/multiple?sublist=2")
#
# driver.maximize_window()
# sleep(2)
# from up to down
# frames=driver.find_element("xpath","//section[@class='flex gap-10 w-full']/div[2]/iframe")

#to down to up
#//section[@class='flex gap-10 w-full']/div[2]/iframe
# driver.switch_to.frame(frames)

# driver.find_element("id","username").send_keys("SuperAdmin@gmail.com")
#
# driver.find_element("id","password").send_keys("SuperAdmin@1234")
#
# driver.find_element("id","submitButton").click()
# sleep(3)

driver.get("https://demoapps.qspiders.com/ui/frames/nestedWithMultiple?sublist=3")

driver.maximize_window()
d1=driver.find_element("xpath","//iframe[@class='w-full h-96']")
driver.switch_to.frame(d1)

d2=driver.find_element("xpath","//div[@class='form_container'][2]/iframe")
driver.switch_to.frame(d2)

# d3=driver.find_element("xpath","//section[@class='main_form_container']/div[2]")
# driver.switch_to.frame(d3)

# d4=driver.find_element("xpath","//section[@class='main_form_container']//div[2]//iframe[1]")
# driver.switch_to.frame(d4)

d5=driver.find_element("xpath","//div[@class='form-group'][1]/iframe[1]")
driver.switch_to.frame(d5)

driver.find_element("xpath","//input[@id='email']").send_keys("Admin@gmail.com")

driver.switch_to.parent_frame()
d6 = driver.find_element("xpath","(//form//iframe)[2]")
driver.switch_to.frame(d6)

driver.find_element("id","password").send_keys("Admin@1234")
driver.switch_to.parent_frame()

d7=driver.find_element("xpath","(//form//iframe)[3]")
driver.switch_to.frame(d7)

driver.find_element("id","confirm").send_keys("Admin@1234")
sleep(2)