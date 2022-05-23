from selenium.webdriver.common.by import By


class ProductsPage:

    URL = "https://www.saucedemo.com/inventory.html"

    # Locators
    logo_class = (By.CLASS_NAME, 'app_logo')
    bike_light_add_button = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')

    # page methods

    def __init__(self, browser):
        self.browser = browser

    def verify_url(self):
        return self.browser.current_url == self.URL

    def verify_logo_display(self):
        return self.browser.find_element(*self.logo_class).is_displayed()

    def add_products_to_cart(self):
        self.browser.find_element(*self.bike_light_add_button).click()

    def verify_cart_count(self):
        count = self.browser.find_element(*self.shopping_cart_badge).text
        print(count)
        return count == 1

