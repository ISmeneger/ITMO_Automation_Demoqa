from selenium.webdriver.support.color import Color
from pages.text_box import TextBox


def test_text_box_submit(browser):
    text_box = TextBox(browser)
    text_box.visit()

    assert Color.from_string(text_box.btn_submit.find_element().value_of_css_property('color')).hex == '#ffffff'

    assert Color.from_string(text_box.btn_submit.find_element().value_of_css_property('background-color')).hex == '#0d6efd'
    assert Color.from_string(text_box.btn_submit.find_element().value_of_css_property('border-top-color')).hex == '#0d6efd'


