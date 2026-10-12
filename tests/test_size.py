from pages.demoqa import DemoQa


def test_size(browser):
    page = DemoQa(browser)
    page.visit()
    browser.set_window_size(1000, 500)
    assert browser.get_window_size() == {'width': 1000, 'height': 500}
    assert page.icon.wait_visible()
