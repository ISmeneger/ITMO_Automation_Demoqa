from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    page = ModalDialogs(browser)
    page.visit()
    page.small_modal.wait_visible()
    assert page.btns_third_menu.check_count_elements(5)


def test_navigation_modal(browser):
    page = ModalDialogs(browser)
    page.visit()
    page.icon.click()
    assert DemoQa(browser).wait_url()
    browser.back()
    assert page.wait_url()
    browser.set_window_size(900, 400)
    browser.forward()
    assert DemoQa(browser).wait_url()
    assert browser.title == 'demosite'
