from pages.text_box import TextBox


def test_placeholder(browser):
    """Проверка значения атрибута элемента"""

    text_box = TextBox(browser)

    text_box.visit()
    assert text_box.name.get_dom_attribute('placeholder') == 'Full Name'