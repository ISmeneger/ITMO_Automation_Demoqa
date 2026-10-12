from pages.base_page import BasePage
from components.components import WebElement


class DemoQa(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/')
        self.icon = WebElement(driver, 'header > a')
        self.btn_elements = WebElement(driver, '.category-cards a[href="/elements"]')
        self.text_footer = WebElement(driver, 'footer > span')
        self.h5 = WebElement(driver, '.category-cards h5')
