import time
import pickle
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


# Fixture for setup and teardown
@pytest.fixture(scope="module")
def setup_teardown():
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.amazon.ae")

    # Load cookies from pickle file (if exists)
    try:
        with open("Login_cookiesss.pkl", "rb") as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        print(" Cookies loaded successfully.")
    except FileNotFoundError:
        print(" Login_cookiesss.pkl not found. Proceeding without loading cookies.")

    yield driver  # Yield control to the test function

    # Clean up
    driver.quit()