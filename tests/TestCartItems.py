import time
import pytest
from selenium.webdriver.common.by import By
from pages.HomePageLocators import HomePageLocators
from utils.ItemsLocators import ItemsLocators
from utils.UtilitiesLocators import UtilitiesLocators

@pytest.mark.usefixtures("setup_teardown")
class TestAddToCart:

    def test_add_item_to_cart(self, setup_teardown):
        driver = setup_teardown
        driver.implicitly_wait(10)
        # We already logged into Amazon account

        # Step 1: Search for the item
        driver.find_element(By.CSS_SELECTOR, HomePageLocators.search_bar).send_keys(UtilitiesLocators.item_name)
        driver.find_element(By.CSS_SELECTOR, HomePageLocators.search_button).click()

        # Step 2: Click on the first search result
        driver.find_element(By.XPATH, ItemsLocators.pen).click()

        # Step 3: Add to cart
        driver.find_element(By.CSS_SELECTOR, UtilitiesLocators.add_to_cart).click()

        # Step 4: Go to cart
        driver.find_element(By.XPATH, UtilitiesLocators.go_to_cart).click()

        # Step 5: Assertion - check item exists in cart
        assert UtilitiesLocators.item_name.lower() in driver.page_source.lower()


        # Screenshot for proof (optional)
        timestamp = time.strftime("%d-%m-%y_%H-%M-%S")
        driver.save_screenshot(f"screenshots/cart_check_{timestamp}.png")