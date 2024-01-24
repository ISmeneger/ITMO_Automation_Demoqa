from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    elements = Accordion(browser)
    elements.visit()

    assert elements.section_1_content.visible()
    elements.section_1_heading.click()
    time.sleep(2)
    assert not elements.section_1_content.visible()

def test_visible_accordion_default(browser):
    elements = Accordion(browser)
    elements.visit()

    assert not elements.section_2_content_1.visible()
    assert not elements.section_2_content_2.visible()
    assert not elements.section_3_content.visible()


