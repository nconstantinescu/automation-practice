from selenium.webdriver.common.by import By


class JsAlerts:
    # URL

    URL = 'https://the-internet.herokuapp.com/javascript_alerts'

    # Locators

    js_alert = (By.CSS_SELECTOR, "li:nth-child(1) > button")
    js_confirm = (By.CSS_SELECTOR, "li:nth-child(2) > button")
    js_prompt = (By.XPATH, "//*[@id=\"content\"]/div/ul/li[3]/button")
    results = (By.ID, "result")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def click_alert(self):
        self.browser.find_element(*self.js_alert).click()

    def click_confirm(self):
        self.browser.find_element(*self.js_confirm).click()

    def click_prompt(self):
        self.browser.find_element(*self.js_prompt).click()

    def result_field(self):
        return self.browser.find_element(*self.results).text
