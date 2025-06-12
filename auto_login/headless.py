from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#import yaml
import time

#with open ("creds.yml", " r ") as file:
#    conf = yaml.safe_load(file)

#options = Options()
#options.add_argument("--headless")
driver = webdriver.Chrome() # remove driver...(options=options)
driver.implicitly_wait(5)

driver.get("https://bandcamp.com/discover")
print(driver.title)

pagination_button = driver.find_element(By.ID, "view-more")
print(pagination_button)

tracks = driver.find_elements(By.CLASS_NAME, "results-grid-item")
print(len(tracks))
print(tracks[0].text)

track_1 = tracks[0]
album = track_1.find_element(By.CSS_SELECTOR, "div.meta a strong")
print(album.text)

time.sleep(2)

driver.close()