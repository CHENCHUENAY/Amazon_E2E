import pickle
import time
from dotenv import load_dotenv
load_dotenv()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.HomePageLocators import HomePageLocators
from pages.LoginPageLocators import LoginPageLocators
from utils.UtilitiesLocators import UtilitiesLocators



# Set up browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.amazon.ae")

wait = WebDriverWait(driver, 20)

# Step 1: Click sign-in (retry logic kept)
# Step 1: Click sign-in with refresh fallback
for _ in range(2):
    try:
        wait.until(EC.element_to_be_clickable((
            By.XPATH, HomePageLocators.signin_option
        ))).click()
        break
    except:
        driver.refresh()


# Step 2:  Enter email

wait.until(
    EC.presence_of_element_located((By.ID, LoginPageLocators.id_))).send_keys(UtilitiesLocators.useridd)

driver.find_element(By.CSS_SELECTOR, LoginPageLocators.contin).click()

# Step 3: Enter password (if appears)
try:
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, LoginPageLocators.pw_))
    ).send_keys(UtilitiesLocators.pw)

    driver.find_element(By.CSS_SELECTOR, LoginPageLocators.signin).click()

except:
    print("Password step skipped to (passkey/OTP flow)")
time.sleep(30)
# Step 4: Wait until login is COMPLETE (state-based)
wait.until(
    EC.text_to_be_present_in_element(
        (By.ID, "nav-link-accountList"),
        "Hello"
    )
)

# Step 5: Save cookies
with open("sessions/Login_cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("Cookies saved successfully")

driver.quit()