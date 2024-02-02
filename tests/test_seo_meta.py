import time
import pytest
from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab

@pytest.mark.parametrize('pages', [Accordion, Alerts, BrowserTab, DemoQa])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == "viewport"
    assert page.viewport.get_dom_attribute('content') == "width=device-width,initial-scale=1"


