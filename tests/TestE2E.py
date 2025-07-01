import time
import pytest
from selenium.webdriver.common.by import By
from pages.HomePageLocators import HomePageLocators
from pages.LoginPageLocators import LoginPageLocators
from utils.ItemsLocators import ItemsLocators
from utils.UtilitiesLocators import UtilitiesLocators
import pickle


class TestLogin:
    @pytest.mark.usefixtures("setup_teardown")
    def test_amazon_purchase(self, setup_teardown):
        # Step 1: Opens Amazon homepage in chrome browser ,done through conftest.py
        driver = setup_teardown  # Getting the WebDriver instance
        driver.implicitly_wait(10)  # Implicit wait for elements to load

        # Step 2: Click on sign-in
        while True:
            try:
                driver.find_element(By.CSS_SELECTOR, HomePageLocators.signin_option).click()
                break  # Exit the loop once the element is found and clicked
            except:
                driver.refresh()  # Refresh the page if the element is not found

        # Step 3: sending login credentials if cookies wont worked
        try:
            driver.find_element(By.CSS_SELECTOR, LoginPageLocators.id_).send_keys(UtilitiesLocators.useridd)
            driver.find_element(By.CSS_SELECTOR, LoginPageLocators.contin).click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, LoginPageLocators.pw_).send_keys(UtilitiesLocators.pw)
            driver.find_element(By.CSS_SELECTOR, LoginPageLocators.signin).click()

            # Step 3: Save cookies for future use
            time.sleep(60)
            with open("Login_cookiesss.pkl", "wb") as f:
                pickle.dump(driver.get_cookies(), f)
                print("Cookies saved to Login_cookiesss.pkl")
        except:
            pass
        # Step 4: Search for an item
        driver.find_element(By.CSS_SELECTOR, HomePageLocators.search_bar).send_keys(UtilitiesLocators.item_name)
        driver.find_element(By.CSS_SELECTOR, HomePageLocators.search_button).click()

        # Step 5: Click on the first search result
        driver.find_element(By.XPATH, ItemsLocators.pen).click()

        # Step 6: Add to cart
        driver.find_element(By.CSS_SELECTOR, UtilitiesLocators.add_to_cart).click()

        # Step 7: Go to cart
        driver.find_element(By.XPATH, UtilitiesLocators.go_to_cart).click()

        # Step 8: Proceed to checkout
        driver.find_element(By.CSS_SELECTOR, UtilitiesLocators.checkout).click()

        # Step 9: Handle "Amazon Prime" suggestion
        try:
            driver.find_element(By.XPATH, UtilitiesLocators.no_prime).click()
        except:
            print("no Prime suggestion popup ")
            pass

        # driver.save_screenshot("./screenshots/final_result.png")
        time.sleep(2)
        timestamp = time.strftime("%d-%m-%y_%H-%M-%S")
        driver.save_screenshot(f"screenshots/passed_{timestamp}.png")

        time.sleep(2)  # Just to confirm the final result


















