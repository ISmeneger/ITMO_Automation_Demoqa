from pages.accordion import Accordion

def test_visible_accordion(browser):
    elements = Accordion(browser)
    elements.visit()

    assert elements.section_1_content.wait_visible()
    elements.section_1_heading.click()

    assert elements.section_1_content.wait_hidden()

def test_visible_accordion_default(browser):
    elements = Accordion(browser)
    elements.visit()

    elements.section_1_content.wait_visible()
    assert not elements.section_2_content_1.visible()
    assert not elements.section_2_content_2.visible()
    assert not elements.section_3_content.visible()


