from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/accordian')
        self.section_1_content = WebElement(driver, '#accordianContainer .accordion-item:nth-child(1) .accordion-body')
        self.section_1_heading = WebElement(driver, '#accordianContainer .accordion-item:nth-child(1) .accordion-button')
        self.section_2_content_1 = WebElement(driver, '#accordianContainer .accordion-item:nth-child(2) .accordion-body')
        self.section_2_content_2 = self.section_2_content_1
        self.section_3_content = WebElement(driver, '#accordianContainer .accordion-item:nth-child(3) .accordion-body')
