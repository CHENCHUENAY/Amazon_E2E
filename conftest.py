import time
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
    driver.maximize_window()  # Maximize the browser window
    # driver.implicitly_wait(10)  # Wait implicitly for elements to be found
    driver.get("https://www.amazon.ae")
    yield driver  # Yield control to the test function

    # Clean up
    driver.quit()