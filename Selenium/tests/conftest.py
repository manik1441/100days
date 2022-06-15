import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default= "chrome"
    )



@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.get.config("browsername")
    driver = None
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=r'/Selenium/drivers/chromedriver.exe')
    elif browser_name == "firefox":
        driver = webdriver.Chrome(executable_path=r'/Selenium/drivers/geckodriver.exe')
    elif browser_name == "ie":
        driver = webdriver.Chrome(executable_path=r'/Selenium/drivers/IEDriverServer.exe')
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
