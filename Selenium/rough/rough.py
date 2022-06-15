import time
from selenium import webdriver

# driver = webdriver.Chrome(ChromeDriverManager.install())
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'/Selenium/drivers/chromedriver.exe')
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()




time.sleep(1000)