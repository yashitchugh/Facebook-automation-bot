from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(5)
driver.maximize_window()
emailElement=driver.find_element(By.XPATH,  '//input[@id="email"]')
emailElement.send_keys("Enter your email here ,eg: xyz@gmail.com")
passElement=driver.find_element(By.XPATH,  '//input[@id="pass"]')
passElement.send_keys(' Enter Password')
time.sleep(5)
elem=driver.find_element(By.NAME,  "login")
elem.click()
time.sleep(25)
# staEle=driver.find_element(By.XPATH, "//div[@role='textbox']")
#
# time.sleep(5)
# staEle.send_keys("Hello there!!")

post_area = driver.find_element(By.XPATH, "//span[contains(text(), \"on your mind\") or contains(text(), \"What's on your mind\")]")
post_area.click()
time.sleep(3)

    # Find the active input area (inside modal)
active_input = driver.find_element(By.XPATH, "//div[@role='textbox']")
active_input.send_keys("Believe in Yourself")

time.sleep(5)
post_button = driver.find_element(By.XPATH, "//div[@aria-label='Post' and @role='button']")
post_button.click()
time.sleep(5)
