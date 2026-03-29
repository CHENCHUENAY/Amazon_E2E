import os


class SharedLocators:
    # Search submit button ID (used as fallback reference)
    search_button = "nav-search-submit-button"

    # Add to Cart button on the product detail page
    add_to_cart = "//button[@id='a-autoid-1-announce']"

    # Proceed to checkout button on the cart page
    proceed_to_checkout = "//input[@name='proceedToRetailCheckout']"

    # Decline warranty/protection plan popup (appears after adding to cart)
    no_thanks = "//input[@aria-labelledby='attachSiNoCoverage-announce']"

    # Decline Amazon Prime upsell popup (appears during checkout flow)
    no_prime = "//*[@id='prime-decline-button']/span/a"

    # Continue button that may appear during checkout flow
    continue_ = "#checkout-byg-ptc-button"

    # Credentials loaded from .env file
    useridd = os.getenv("AMAZON_USERNAME")
    pw = os.getenv("AMAZON_PASSWORD")


def validate_credentials():
    """Raises an error if Amazon credentials are not set in the .env file."""
    if not SharedLocators.useridd or not SharedLocators.pw:
        raise RuntimeError("AMAZON_USERNAME / AMAZON_PASSWORD not set in .env")