from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Entry:
    # URL
    URL = 'https://the-internet.herokuapp.com/'

    # Locators

    entry_ad_link = (By.LINK_TEXT, 'Entry Ad')
    ad_window = (By.CLASS_NAME, 'modal')
    close_button = (By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p')
    click_here_button = (By.LINK_TEXT, "click here")
    key_placeholder = (By.LINK_TEXT, 'Elemental Selenium')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def load(self):
        self.browser.get(self.URL)

    def click_entry_ad(self):
        self.browser.find_element(*self.entry_ad_link).click()

    def ad_pop_up(self):
        return self.browser.find_element(*self.ad_window)

    def click_close(self):
        self.browser.find_element(*self.close_button).click()

    def refresh(self):
        self.browser.find_element(*self.key_placeholder).send_keys(Keys.COMMAND + 'r')

    def click_here(self):
        self.browser.find_element(*self.click_here_button).click()







