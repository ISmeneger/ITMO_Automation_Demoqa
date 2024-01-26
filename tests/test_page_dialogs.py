from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa

def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()

    assert modal_dialogs.btns_third_menu.check_count_elements(5)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    demo = DemoQa(browser)

    modal_dialogs.visit()

    modal_dialogs.refresh()
    modal_dialogs.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()

    assert demo.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)





