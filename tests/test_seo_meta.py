import pytest
from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab

@pytest.mark.parametrize('pages', [Accordion, Alerts, BrowserTab, DemoQa])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()


    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == "viewport"
    content = page.viewport.get_dom_attribute('content')
    settings = dict(part.strip().split('=', 1) for part in content.split(','))
    assert settings['width'].strip() == 'device-width'
    assert float(settings['initial-scale']) == 1.0


