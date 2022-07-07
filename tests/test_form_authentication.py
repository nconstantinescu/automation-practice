""" Work in progress. Need to add some sort of method to hide sensitive
information(users/passwords) from test results """

import json
import pytest
from objects.form_authentication import Authentication

with open('hidden.json') as hid:
    hidden = json.load(hid)
username = hidden['user']
password = hidden['password']


def test_successful_authentication(browser):
    authenticate = Authentication(browser)

    # Given that "The Internet" page loads
    authenticate.load()

    # When the user navigates to "Form Authentication"
    authenticate.click_form_authentication()

    # And enters the correct user and password combination

    authenticate.input(username, password)
    authenticate.click_login()

    # Then the " You logged into a secure area!" message and Logout buttons appear
    assert "You logged into a secure area!" in authenticate.valid_input_message()
    assert authenticate.logout().is_displayed()

    # And they can press the Logout button to return to the login screen
    authenticate.click_logout()
    assert authenticate.login().is_displayed()


@pytest.mark.parametrize("wrong_user, wrong_password",
                         [(username, "password"), ("test", password), ("", ""), (username, ""), ("", password)])
def test_unsuccessful_authentication(browser, wrong_user, wrong_password):
    authenticate = Authentication(browser)

    # Given that "The Internet" page loads
    authenticate.load()

    # When the user navigates to "Form Authentication"
    authenticate.click_form_authentication()

    # And enter the incorrect user and/or password
    authenticate.input(wrong_user, wrong_password)
    authenticate.click_login()

    # Then the "Your username is invalid!" or "Your password is invalid!" message appears
    if wrong_user == username and wrong_password != password:
        assert "Your password is invalid!" in authenticate.invalid_input_message()
    elif wrong_user != username and wrong_password == password:
        assert "Your username is invalid!" in authenticate.invalid_input_message()
    elif wrong_user != username and wrong_password != password:
        assert "Your username is invalid!" in authenticate.invalid_input_message()
