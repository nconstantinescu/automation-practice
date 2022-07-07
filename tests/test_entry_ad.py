""""Work in Progress. The test only seems to pass on headless browsers,
it might be a bug from the website (the pop-up fails to appear most of the time
after pressing click here(or reloading) even while manually testing"""

from objects.entry_ad import Entry
import selenium.webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = selenium.webdriver.ChromeOptions()
opts.add_argument('headless')
browsers = selenium.webdriver.Chrome(options=opts)


def test_ad():
    ad = Entry(browsers)

    # Given that the "the-internet" page loads
    ad.load()
    # When the user navigates to "Entry Ad"
    ad.click_entry_ad()

    # Then an ad pop-up appears
    wait = WebDriverWait(browsers, 5)
    wait.until(EC.element_to_be_clickable(ad.ad_pop_up()))
    assert ad.ad_pop_up().is_displayed()

    # And after closing it the ad no longer appears on page load
    ad.click_close()
    ad.refresh()
    assert not ad.ad_pop_up().is_displayed()

    browsers.back()
    browsers.forward()
    assert not ad.ad_pop_up().is_displayed()

    # And the ad appears again after pressing "click here"
    ad.click_here()
    wait.until(EC.element_to_be_clickable(ad.ad_pop_up()))
    assert ad.ad_pop_up().is_displayed()
