from pages.demoqa import DemoQa
from pages.elements import Elements


def test_go_to_page_elements(browser):
    demo = DemoQa(browser)
    demo.visit()
    assert demo.equal_url()
    demo.btn_elements.click()
    assert Elements(browser).wait_url()
