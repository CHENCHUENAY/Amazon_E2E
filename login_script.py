# To save_Login_cookies.py

import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.HomePageLocators import HomePageLocators
from pages.LoginPageLocators import LoginPageLocators
from utils.UtilitiesLocators import UtilitiesLocators

# Set up browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to Amazon login page
driver.get("https://www.amazon.ae/")

# Step 2: Click on sign-in
while True:
    try:
        driver.find_element(By.CSS_SELECTOR, HomePageLocators.signin_option).click()
        break  # Exit the loop once the element is found and clicked
    except:
        driver.refresh()  # Refresh the page if the element is not found
try:
    driver.find_element(By.CSS_SELECTOR, LoginPageLocators.id_).send_keys(UtilitiesLocators.useridd)
    driver.find_element(By.CSS_SELECTOR, LoginPageLocators.contin).click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, LoginPageLocators.pw_).send_keys(UtilitiesLocators.pw)
    driver.find_element(By.CSS_SELECTOR, LoginPageLocators.signin).click()
except:
    pass

#  Give time to log in manually
time.sleep(40)

# Save cookies to file
with open("Login_cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)
    print("Cookies saved to Login_cookies.pkl")

driver.quit()


