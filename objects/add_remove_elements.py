from selenium.webdriver.common.by import By


class AddRemove:
    # URL

    URL = 'https://the-internet.herokuapp.com/add_remove_elements/'

    # Locators

    add_elements = (By.XPATH, '//*[@id="content"]/div/button')
    remove_elements = (By.CLASS_NAME, 'added-manually')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)


    def click_add(self):
        self.browser.find_element(*self.add_elements).click()

    def find_remove(self):
        found = self.browser.find_elements(*self.remove_elements)
        return found

    def click_remove(self):
        delete_buttons = self.browser.find_elements(*self.remove_elements)
        for buttons in delete_buttons:
            buttons.click()
