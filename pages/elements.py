from pages.base_page import BasePage
from components.components import WebElement


class Elements(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/elements')
        self.text_please = WebElement(driver, '.playgound-body .col-xl-7')
        self.icon = WebElement(driver, 'header > a > img')
        self.btn_sidebar_first = WebElement(driver, '.element-group:first-child .group-header')
        self.btn_sidebar_first_textbox = WebElement(driver, '.element-group:first-child a[href="/text-box"]')
        self.btn_sidebar_first_checkbox = WebElement(driver, '.element-group:first-child a[href="/checkbox"]')
        self.btns_first_menu = WebElement(driver, '.element-group:first-child .menu-list li')
