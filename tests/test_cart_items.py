import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.HomePageLocators import HomePageLocators
from utils.ProductLocators import ProductLocators
from utils.SharedLocators import SharedLocators


@pytest.mark.usefixtures("setup_teardown")
class TestAddToCart:

    def test_add_item_to_cart(self, setup_teardown):
        driver = setup_teardown
        wait = WebDriverWait(driver, 20)

        # Step 1: Clear any previous input and search for the target product
        search = wait.until(EC.element_to_be_clickable((By.XPATH, HomePageLocators.search_bar_field)))
        search.clear()
        search.send_keys(ProductLocators.item_name)
        driver.find_element(By.XPATH, HomePageLocators.search_button).click()

        # Step 2: Click the target product from search results
        wait.until(EC.element_to_be_clickable((
            By.XPATH, ProductLocators.item_locator))).click()

        # Step 3: Click Add to Cart on the product detail page
        wait.until(EC.element_to_be_clickable((
            By.XPATH, SharedLocators.add_to_cart))).click()

        # Step 4: Navigate to the cart using the fixed cart icon in the header
        wait.until(EC.element_to_be_clickable((
            By.XPATH, HomePageLocators.go_to_cart))).click()

        # Step 5: Verify the product name appears in the cart page source
        assert ProductLocators.item_name.lower() in driver.page_source.lower(), \
            f"Expected '{ProductLocators.item_name}' in cart but not found"

        # Step 6: Capture screenshot as evidence of successful cart addition
        timestamp = time.strftime("%d-%m-%y_%H-%M-%S")
        driver.save_screenshot(f"screenshots/passed/cart_passed_{timestamp}.png")