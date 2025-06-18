import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pickle

# Fixture for setup and teardown
@pytest.fixture(scope="module")
def setup_teardown():

    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()  # Maximize the browser window
    # driver.implicitly_wait(10)  # Wait implicitly for elements to be found
    driver.get("https://www.amazon.ae")

    # Loading cookies with user credentials in amazon
    try:
        with open("Login_cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                if 'sameSite' in cookie:
                    del cookie['sameSite']
                try:
                    driver.add_cookie(cookie)
                except Exception as e:
                    print(f"️ Skipping one cookie: {e}")
        driver.refresh()
        print(" Cookies loaded and session refreshed")

    except FileNotFoundError:
        print(" Cookie file not found. Run the login script to create it.")




    yield driver  # Yield control to the test function

    # Clean up
    driver.quit()