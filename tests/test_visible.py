from pages.elements import Elements
import time

def test_visible_btn_sidebar(browser):
    elements = Elements(browser)
    elements.visit()
    # elements.btn_sidebar_first.click()
    # time.sleep(3)
    # assert elements.btn_sidebar_first_textbox.exist()
    assert elements.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    elements = Elements(browser)
    elements.visit()

    assert elements.btn_sidebar_first_checkbox.visible()
    elements.btn_sidebar_first.click()
    time.sleep(3)
    assert not elements.btn_sidebar_first_checkbox.visible()


