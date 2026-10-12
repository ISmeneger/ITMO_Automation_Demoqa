from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from pages.slider import Slider


def test_slider_v1(browser):
    page = Slider(browser)
    page.visit()
    assert page.slider.exist()
    page.slider.send_keys(Keys.HOME)
    for _ in range(50):
        page.slider.send_keys(Keys.ARROW_RIGHT)
    WebDriverWait(browser, 10).until(lambda _: page.inp.get_value() == '50')
    assert page.slider.get_value() == '50'
