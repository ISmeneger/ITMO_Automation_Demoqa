from selenium.webdriver.support.ui import WebDriverWait
from pages.progress_bar import ProgressBar


def test_progress_bar(browser):
    page = ProgressBar(browser)
    page.visit()
    page.start_stop_button.click()
    WebDriverWait(browser, 15).until(
        lambda _: int(page.progress_bar.get_dom_attribute('aria-valuenow')) >= 50)
    page.start_stop_button.click()
    value = int(page.progress_bar.get_dom_attribute('aria-valuenow'))
    assert 50 <= value <= 100
    assert page.start_stop_button.get_text() == 'Start'
