from objects.javascript_alerts import JsAlerts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_al(browsers):
    alerts = JsAlerts(browsers)
    # Given that the "JavaScript Alerts" page of "the-internet" website loads
    alerts.load()

    # When the user clicks the JS Alert button
    alerts.click_alert()

    # Then a message indicating the performed action appears under "Result:"
    WebDriverWait(browsers, 10).until(EC.alert_is_present())
    browsers.switch_to.alert.accept()
    assert "You successfully clicked an alert" in alerts.result_field()


def test_confirm(browsers):
    alerts = JsAlerts(browsers)

    # Given that the "JavaScript Alerts" page of "the-internet" website loads
    alerts.load()

    # When the user clicks the JS Confirm button
    alerts.click_confirm()

    # Then a message indicating the performed action appears under "Result:"
    browsers.switch_to.alert.accept()
    assert "Ok" in alerts.result_field()

    alerts.click_confirm()
    browsers.switch_to.alert.dismiss()
    assert "Cancel" in alerts.result_field()


def test_prompt(browsers, word="test"):
    alerts = JsAlerts(browsers)

    # Given that the "JavaScript Alerts" page of "the-internet" website loads
    alerts.load()

    # When the user clicks the JS Prompt button
    alerts.click_prompt()

    # Then a message indicating the performed action appears under "Result:"
    WebDriverWait(browsers, 10).until(EC.alert_is_present())
    browsers.switch_to.alert.send_keys(word)
    browsers.switch_to.alert.accept()
    assert word in alerts.result_field()

    alerts.click_prompt()
    browsers.switch_to.alert.accept()
    assert "You entered:" in alerts.result_field()

    alerts.click_prompt()
    browsers.switch_to.alert.dismiss()
    assert "null" in alerts.result_field()
