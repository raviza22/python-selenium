from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:

    # Base URL
    URL = "https://www.saucedemo.com/"

    # Test data
    username = "standard_user"
    password = "secret_sauce"

    # Locators
    username_input = (By.ID, 'user-name')
    password_input = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    # page methods

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def login(self):
        self.browser.find_element(*self.username_input).clear()
        self.browser.find_element(*self.username_input).send_keys(self.username)
        self.browser.find_element(*self.password_input).clear()
        self.browser.find_element(*self.password_input).send_keys(self.password)
        self.browser.find_element(*self.login_button).click()

    def title(self):
        return self.browser.title
