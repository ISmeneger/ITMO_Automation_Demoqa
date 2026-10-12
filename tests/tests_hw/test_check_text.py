from pages.demoqa import DemoQa
from pages.elements import Elements


def test_check_text_footer(browser):
    page = DemoQa(browser)
    page.visit()
    year = browser.execute_script('return new Date().getFullYear()')
    assert page.text_footer.get_text() == f'© 2013-{year} TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_page_elements(browser):
    page = Elements(browser)
    page.visit()
    assert 'Please select an item from left to start practice.' in page.text_please.get_text()
    assert page.icon.wait_visible()
    assert page.btn_sidebar_first.wait_visible()
    assert page.btn_sidebar_first_textbox.wait_visible()
