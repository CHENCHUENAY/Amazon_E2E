import os
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.HomePageLocators import HomePageLocators
from utils.ProductLocators import ProductLocators
from utils.SharedLocators import SharedLocators


@pytest.mark.usefixtures("setup_teardown")
class TestAmazonE2E:

    def test_purchase_flow(self, setup_teardown):
        driver = setup_teardown
        wait = WebDriverWait(driver, 25)

        # Step 1: Clear any previous input and search for the target product
        search = wait.until(EC.element_to_be_clickable((By.XPATH, HomePageLocators.search_bar_field)))
        search.clear()
        search.send_keys(ProductLocators.item_name)
        driver.find_element(By.XPATH, HomePageLocators.search_button).click()

        # Step 2: Click the exact target product from search results
        wait.until(EC.element_to_be_clickable((
            By.XPATH, ProductLocators.item_locator))).click()

        # Step 3: Click Add to Cart on the product detail page
        wait.until(EC.element_to_be_clickable((
            By.XPATH, SharedLocators.add_to_cart))).click()

        # Step 4: Dismiss warranty/protection popup if it appears
        try:
            wait.until(EC.presence_of_element_located((
                By.XPATH, SharedLocators.no_thanks))).click()
        except Exception:
            pass  # Popup did not appear — continue normally

        # Step 5: Refresh to reset DOM state after cart interaction
        driver.refresh()

        # Step 6: Navigate to cart using the fixed cart icon in the header
        wait.until(EC.element_to_be_clickable((
            By.XPATH, HomePageLocators.go_to_cart))).click()

        # Step 7: Capture screenshot as evidence of successful cart flow
        os.makedirs("screenshots/passed", exist_ok=True)
        driver.save_screenshot(f"screenshots/passed/e2e_cart_{int(time.time())}.png")

        # Step 8: Click Proceed to Checkout
        wait.until(EC.element_to_be_clickable((
            By.XPATH, SharedLocators.proceed_to_checkout))).click()

        # Step 9: Handle optional continue button that may appear mid-checkout
        try:
            wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, SharedLocators.continue_))).click()
        except Exception:
            pass  # Continue button did not appear — proceed to assertion

        # Step 10: Assert flow reached checkout or re-auth page
        # Amazon requires re-authentication before payment on automated sessions
        assert "signin" in driver.current_url.lower() or "checkout" in driver.current_url.lower(), \
            f"Expected checkout or signin redirect, got: {driver.current_url}"