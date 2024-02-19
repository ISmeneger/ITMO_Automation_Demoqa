import time
import pytest
from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab


def test_seo(browser):
    demo = DemoQa(browser)

    demo.visit()
    assert browser.title == 'DEMOQA'

# Декоратор @pytest.mark.parametrize() для цикличных тестов с разными переменными.
# Мы можем передать классы страниц, как переменную для теста
@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.get_title() == 'DEMOQA'