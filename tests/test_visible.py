from pages.elements import Elements


def test_visible_btn_sidebar(browser):
    page = Elements(browser)
    page.visit()
    assert page.btn_sidebar_first_textbox.wait_visible()


def test_not_visible_btn_sidebar(browser):
    page = Elements(browser)
    page.visit()
    page.btn_sidebar_first_checkbox.wait_visible()
    page.btn_sidebar_first.click()
    assert page.btn_sidebar_first_checkbox.wait_hidden()
