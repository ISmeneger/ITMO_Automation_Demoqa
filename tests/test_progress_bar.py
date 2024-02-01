import time
from pages.progress_bar import ProgressBar


def test_progress_bar(browser):
    page_progress_bar = ProgressBar(browser)
    page_progress_bar.visit()
    time.sleep(2)

    page_progress_bar.start_stop_button.click()

    while True:
        if page_progress_bar.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            page_progress_bar.start_stop_button.click()
            break

    time.sleep(2)

    assert page_progress_bar.progress_bar.get_dom_attribute('aria-valuenow') == '51'