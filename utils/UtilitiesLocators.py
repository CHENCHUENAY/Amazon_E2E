import conftest
class UtilitiesLocators:
    add_to_cart = '[id="add-to-cart-button"]'
    go_to_cart = "//a[@id='nav-cart']"
    # go_to_cart = "//span[@class='nav-line-2'][normalize-space()='Cart']"
    no_thanks = "//span[@class='a-button-inner']//span[@id='attachSiNoCoverage-announce' and text()='No Thanks']"
    checkout= '[name="proceedToRetailCheckout"]'

    no_prime = '// *[ @ id = "prime-decline-button"] / span / a'   #"//a[@id='prime-declineCTA' and contains(text(), 'No thanks, continue without Prime')]"
    # '// *[ @ id = "prime-decline-button"] / span / a'

    item_name="Parker Frontier Matte Black (Gold Nib) GT Fountain Pen, 1 Count (Pack of 1) (9000020642)"

    # Credentials1@
    useridd='chenchuenay@gmail.com'
    pw='ChenchuEnay1@'

