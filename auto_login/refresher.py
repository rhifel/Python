from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

interval = 5 # seconds

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options) # 


driver.get("https://practicetestautomation.com")

print(driver.page_source)

try:
    while True:
        print("refreshing...")
        driver.refresh()
        print("done")
        time.sleep(interval)

except KeyboardInterrupt:
    pass

driver.quit()