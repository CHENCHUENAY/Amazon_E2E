import time
import pytest
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
from pages.HomePageLocators import HomePageLocators
from pages.LoginPageLocators import LoginPageLocators
from utils.ItemsLocators import ItemsLocators
from utils.UtilitiesLocators import UtilitiesLocators


class TestLogin:
    @pytest.mark.usefixtures("setup_teardown")
    def test_amazon_purchase(self, setup_teardown):
        driver = setup_teardown  # Getting the WebDriver instance
        driver.implicitly_wait(10)  # Implicit wait for elements to load

        # Step 1: Open Amazon homepage
        driver.get("https://www.amazon.ae")

        # Step 2: Click on sign-in
        driver.find_element(By.CSS_SELECTOR, HomePageLocators.signin_option).click()

        # Step 3: Enter login credentials
        driver.find_element(By.CSS_SELECTOR, LoginPageLocators.id_).send_keys(UtilitiesLocators.useridd)
        driver.find_element(By.CSS_SELECTOR, LoginPageLocators.contin).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, LoginPageLocators.pw_).send_keys(UtilitiesLocators.pw)
        driver.find_element(By.CSS_SELECTOR, LoginPageLocators.signin).click()

        # Step 4: Search for an item
        driver.find_element(By.CSS_SELECTOR, HomePageLocators.search_bar).send_keys(UtilitiesLocators.item_name)
        driver.find_element(By.CSS_SELECTOR, HomePageLocators.search_button).click()

        # Step 5: Click on the first search result
        driver.find_element(By.XPATH, ItemsLocators.oneplus_13r).click()

        # Step 6: Add to cart
        driver.find_element(By.CSS_SELECTOR, UtilitiesLocators.add_to_cart).click()

        # Step 7: Go to cart
        driver.find_element(By.CSS_SELECTOR, UtilitiesLocators.go_to_cart).click()

        # Step 8: Proceed to checkout
        driver.find_element(By.CSS_SELECTOR, UtilitiesLocators.checkout).click()

        # Step 9: Handle "Amazon Prime" suggestion
        try:
            driver.find_element(By.XPATH, UtilitiesLocators.no_prime).click()
        except:
            print("no Prime suggestion popup ")
            pass
        driver.save_screenshot("reports/screenshots/final_result.png")

        time.sleep(5)  # Just to confirm the final result
















#
# import time
# import pytest
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from pages.HomePageLocators import HomePageLocators
# from pages.LoginPageLocators import LoginPageLocators
# from utils.ItemsLocators import ItemsLocators
# from utils.UtilitiesLocators import UtilitiesLocators
#
#
# class TestLogin:
#     @pytest.mark.usefixtures("setup_teardown")
#     def test_amazon_purchase(self, setup_teardown, request):
#         driver = setup_teardown  # Getting the WebDriver instance
#         driver.implicitly_wait(10)  # Implicit wait for elements to load
#
#         # ✅ Get pytest_html plugin properly
#         pytest_html = request.config.pluginmanager.getplugin('html')
#         extra = getattr(request.node, "extra", [])
#
#         # Step 1: Open Amazon homepage
#         driver.get("https://www.amazon.ae")
#         extra.append(pytest_html.extras.text("Opened Amazon homepage"))
#
#         # Step 2: Click on sign-in
#         driver.find_element(By.CSS_SELECTOR, HomePageLocators.signin_option).click()
#         extra.append(pytest_html.extras.text("Clicked on Sign In"))
#
#         # Step 3: Enter login credentials
#         driver.find_element(By.CSS_SELECTOR, LoginPageLocators.id_).send_keys(UtilitiesLocators.useridd)
#         driver.find_element(By.CSS_SELECTOR, LoginPageLocators.contin).click()
#         time.sleep(2)
#         driver.find_element(By.CSS_SELECTOR, LoginPageLocators.pw_).send_keys(UtilitiesLocators.pw)
#         driver.find_element(By.CSS_SELECTOR, LoginPageLocators.signin).click()
#         extra.append(pytest_html.extras.text("Logged in successfully"))
#
#         # Step 4: Search for an item
#         driver.find_element(By.CSS_SELECTOR, HomePageLocators.search_bar).send_keys(UtilitiesLocators.item_name)
#         driver.find_element(By.CSS_SELECTOR, HomePageLocators.search_button).click()
#         extra.append(pytest_html.extras.text(f"Searched for item: {UtilitiesLocators.item_name}"))
#
#         # Step 5: Click on the first search result
#         driver.find_element(By.XPATH, ItemsLocators.oneplus_13r).click()
#         extra.append(pytest_html.extras.text("Clicked on first search result"))
#
#         # Step 6: Add to cart
#         driver.find_element(By.CSS_SELECTOR, UtilitiesLocators.add_to_cart).click()
#         extra.append(pytest_html.extras.text("Added item to cart"))
#
#         # Step 7: Go to cart
#         driver.find_element(By.CSS_SELECTOR, UtilitiesLocators.go_to_cart).click()
#         extra.append(pytest_html.extras.text("Navigated to cart"))
#
#         # Step 8: Proceed to checkout
#         driver.find_element(By.CSS_SELECTOR, UtilitiesLocators.checkout).click()
#         extra.append(pytest_html.extras.text("Proceeded to checkout"))
#
#         # Step 9: Handle "Amazon Prime" suggestion
#         driver.find_element(By.XPATH, UtilitiesLocators.no_prime).click()
#         extra.append(pytest_html.extras.text("Skipped Amazon Prime suggestion"))
#
#         time.sleep(5)  # Just to confirm the final result
#
#         # ✅ Capture a screenshot on test completion
#         extra.append(pytest_html.extras.image(driver.get_screenshot_as_base64(), "Final Screenshot"))
#
