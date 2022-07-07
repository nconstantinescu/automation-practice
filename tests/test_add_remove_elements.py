from objects.add_remove_elements import AddRemove


def test_add_remove(browser):
    add_remove = AddRemove(browser)

    #  Given that the "Add/Remove Elements" page of "the-internet" loads
    add_remove.load()

    # When the user presses the Add button multiple times
    for i in range(5):
        add_remove.click_add()

    # Then the Delete buttons appear
    assert add_remove.find_remove()

    # And pressing the Delete buttons makes them disappear
    add_remove.click_remove()
    assert not add_remove.find_remove()
