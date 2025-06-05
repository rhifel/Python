from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#import yaml
import time

#with open ("creds.yml", " r ") as file:
#    conf = yaml.safe_load(file)

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.get("https://bandcamp.com/discover")

Title = driver.title

print(Title)

time.sleep(2)

driver.close()