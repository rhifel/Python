from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver_path = ChromeDriverManager().install()
print("ChromeDriver path:", driver_path)

driver.get("https://www.google.com/")

time.sleep(3)

driver.quit()