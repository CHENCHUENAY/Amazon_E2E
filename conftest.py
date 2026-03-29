import time
import pickle
import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def setup_teardown():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://www.amazon.ae")

    cookie_path = "sessions/Login_cookies.pkl"

    if not os.path.exists(cookie_path):
        raise Exception("Cookies not found. Run login_script.py first.")

    with open(cookie_path, "rb") as f:
        cookies = pickle.load(f)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    result = outcome.get_result()
    
    driver = item.funcargs.get("setup_teardown")
    if result.when == "call" and result.failed:
        if driver:
            os.makedirs("screenshots/failed", exist_ok=True)
            filename = f"screenshots/failed/failed_{int(time.time())}.png"
            driver.save_screenshot(filename)
            print(f"Screenshot saved: {filename}")

    # elif result.when == "call" and result.passed:
    #     if driver:
    #         os.makedirs("screenshots/passed", exist_ok=True)
    #         filename = f"screenshots/passed/passed_{int(time.time())}.png"
    #         driver.save_screenshot(filename)
    #         print(f"Screenshot saved: {filename}")