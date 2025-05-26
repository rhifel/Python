from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
import time

with open("creds.yml", "r") as file:
    conf = yaml.safe_load(file)

myTEST_email = conf['test_user']['Username']
myTEST_pass = conf['test_user']['Password']

driver = webdriver.Chrome()
driver.implicitly_wait(2)

def auto_BOT(url, username_locator, username, password_locator, password, submit_locator):
    
    driver.get(url)
    driver.find_element(By.ID, username_locator).send_keys(username)
    driver.find_element(By.ID, password_locator).send_keys(password)
    driver.find_element(By.ID, submit_locator).click()


auto_BOT("https://practicetestautomation.com/practice-test-login/", 
        "username", myTEST_email,
        "password", myTEST_pass, 
        "submit"
)

time.sleep(3)

driver.close()