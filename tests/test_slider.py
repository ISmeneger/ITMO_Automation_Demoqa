from selenium.webdriver import Keys
from pages.slider import Slider


# Данный тест с таким решением не проходит
# def test_slider_v1(browser):
#     slider = Slider(browser)
#
#     slider.visit()
#     assert slider.slider.exist()
#     assert slider.inp.exist()
#
#     slider.inp.send_keys('50')
#     slider.slider.send_keys('50')
#
#     assert slider.inp.get_dom_attribute('value') == '50'

def test_slider_v1(browser):
    page_slider = Slider(browser)
    page_slider.visit()
    assert page_slider.slider.exist()
    assert page_slider.inp.exist()

    while not page_slider.inp.get_dom_attribute('value') == '50':
        page_slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert page_slider.slider.get_dom_attribute('value') == '50'


