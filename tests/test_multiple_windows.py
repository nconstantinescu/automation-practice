from objects.multiple_windows import Windows


def test_windows(browser):
    win = Windows(browser)

    # Given that the "Context Menu" page of "the-internet" loads
    win.load()

    # When the user clicks the "Click Here" hyperlink
    win.click()

    # Then a new tab that contains the text "New Window" is opened
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url in win.new_url()
    assert 'New Window' in win.new_window()
