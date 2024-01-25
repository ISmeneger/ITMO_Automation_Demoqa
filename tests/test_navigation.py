from pages.demoqa import DemoQa
from pages.elements import Elements


def test_navigation(browser):
    demo = DemoQa(browser)
    elements = Elements(browser)

    demo.visit()
    demo.btn_elements.click()

    elements.refresh()
    browser.refresh()

    browser.back()
    browser.forward()
    assert elements.equal_url()
