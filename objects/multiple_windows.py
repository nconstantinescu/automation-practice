from selenium.webdriver.common.by import By


class Windows:

    # URL

    URL = 'https://the-internet.herokuapp.com/windows'
    URL_new = 'https://the-internet.herokuapp.com/windows/new'

    # Locators

    click_here = (By.CSS_SELECTOR, '.example a')
    new = (By.XPATH, '//div[@class=\'example\']/h3[text()=\'New Window\']')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def load(self):
        self.browser.get(self.URL)

    def click(self):
        self.browser.find_element(*self.click_here).click()

    def new_window(self):
        return self.browser.find_element(*self.new).text

    def new_url(self):
        return self.URL_new