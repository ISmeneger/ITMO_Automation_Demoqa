import time
from pages.links import Links


# Задача 4.
def test_window_tab(browser):
    page_links = Links(browser)
    page_links.visit()

    assert page_links.home_link.get_text() == 'Home'
    time.sleep(2)
    assert page_links.home_link.get_dom_attribute('href') == 'https://demoqa.com'

    page_links.home_link.click()
    time.sleep(2)

    assert len(browser.window_handles) == 2



