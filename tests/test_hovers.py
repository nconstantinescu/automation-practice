from objects.hovers import Hover
from selenium.webdriver.common.action_chains import ActionChains


def test_hover(browsers):
    hover = Hover(browsers)
    action = ActionChains(browsers)
    # Given that the "Hovers" page of "the-internet" website loads
    hover.load()

    # When the hovers over each profile icon with their mouse
    action.move_to_element(hover.figure()).perform()

    # Then the correct names and links appear on the screen
    assert "name: user1" in hover.user()
    assert 'https://the-internet.herokuapp.com/users/1' in hover.profile()

    action.move_to_element(hover.figure()).perform()
    assert "name: user2" in hover.user()
    assert 'https://the-internet.herokuapp.com/users/2' in hover.profile()

    action.move_to_element(hover.figure()).perform()
    assert "name: user3" in hover.user()
    assert 'https://the-internet.herokuapp.com/users/3' in hover.profile()
