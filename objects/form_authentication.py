from selenium.webdriver.common.by import By


class Authentication:
    # URL

    URL = 'https://the-internet.herokuapp.com/'

    # Locators

    form_authentication_link = (By.LINK_TEXT, 'Form Authentication')
    login_button = (By.CLASS_NAME, 'radius')
    username_input = (By.ID, 'username')
    password_input = (By.NAME, 'password')
    invalid_input = (By.CLASS_NAME, 'flash')
    valid_input = (By.ID, 'flash')
    logout_button = (By.XPATH, '//*[@id="content"]/div/a')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def load(self):
        self.browser.get(self.URL)

    def click_form_authentication(self):
        self.browser.find_element(*self.form_authentication_link).click()

    def valid_input_message(self):
        return self.browser.find_element(*self.valid_input).text

    def invalid_input_message(self):
        return self.browser.find_element(*self.invalid_input).text

    def input(self, user, passw):
        self.browser.find_element(*self.username_input).send_keys(user)
        self.browser.find_element(*self.password_input).send_keys(passw)

    def click_login(self):
        self.browser.find_element(*self.login_button).click()

    def logout(self):
        return self.browser.find_element(*self.logout_button)

    def login(self):
        return self.browser.find_element(*self.login_button)

    def click_logout(self):
        self.browser.find_element(*self.logout_button).click()
