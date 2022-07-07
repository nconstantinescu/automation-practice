from selenium.webdriver.common.by import By


class Hover:
    nums = iter([3, 4, 5])
    nums2 = iter([3, 4, 5])
    nums3 = iter([3, 4, 5])
    # URL
    URL = 'https://the-internet.herokuapp.com/hovers'

    # Locators
    """Copy these selectors directly in their respective methods.
    Each time you call the method, it will iterate to the next element"""
    # figure = (By.CSS_SELECTOR, f'.figure:nth-child({next(nums)})')
    # user = (By.CSS_SELECTOR, 'f'.figure:nth-child({next(nums2)}) h5')
    # profile = (By.CSS_SELECTOR, 'f'.figure:nth-child({next(nums2)}) a')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def load(self):
        self.browser.get(self.URL)

    def figure(self):
        return self.browser.find_element(By.CSS_SELECTOR, f'.figure:nth-child({next(Hover.nums)})')

    def user(self):
        return self.browser.find_element(By.CSS_SELECTOR, f'.figure:nth-child({next(Hover.nums2)}) h5').text

    def profile(self):
        profile_element = self.browser.find_element(By.CSS_SELECTOR, f'.figure:nth-child({next(Hover.nums3)}) a')
        return profile_element.get_attribute('href')
