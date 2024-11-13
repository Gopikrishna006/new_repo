import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.fixture()
def launch_and_close():
    serv=Service("C:\Python_Selenium\Drivers\chromedriver.exe")
    driver=WebDriver()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/login")
    print('launch')
    yield
    driver.close()

@pytest.mark.priority1
def test_login(launch_and_close):
    print('execute login')

@pytest.mark.priority2
def test_close_it(launch_and_close):
    print('it is closed')

