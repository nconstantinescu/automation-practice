from objects.context_menu import Context
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_context(browsers):
    context = Context(browsers)

    # Given that the "Context Menu" page of "the-internet" loads

    context.load()

    # When the user right-clicks the context menu box
    ActionChains(browsers).context_click(context.menu()).perform()
    # A simple JavaScript alert is triggered and interactable
    assert "You selected a context menu" in browsers.switch_to.alert.text
    browsers.switch_to.alert.accept()
    try:
        WebDriverWait(browsers, 2).until(EC.alert_is_present())
        no_alert = False
    except:
        no_alert = True

    assert no_alert
