from selenium.webdriver.common.by import By


class Context:
    # URL
    URL = 'https://the-internet.herokuapp.com/context_menu'

    # Locators

    hot_spot = (By.ID, 'hot-spot')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def load(self):
        self.browser.get(self.URL)

    def menu(self):
        return self.browser.find_element(*self.hot_spot)
