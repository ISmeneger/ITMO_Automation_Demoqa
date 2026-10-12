from pages.text_box import TextBox


def test_clear(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('tester')

    text_box.name.clear()

    assert text_box.name.get_value() == ''