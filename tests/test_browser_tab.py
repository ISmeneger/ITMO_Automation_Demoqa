from selenium.webdriver.support.ui import WebDriverWait
from pages.browser_tab import BrowserTab


def test_browser_tab(browser):
    page_browser = BrowserTab(browser)
    page_browser.visit()

    assert len(browser.window_handles) == 1

    page_browser.new_tab.click()


    WebDriverWait(browser, 10).until(lambda d: len(d.window_handles) == 2)
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])

