from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_third_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, 'header > a > img')
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.close_small_modal = WebElement(driver, '#closeSmallModal')
        self.close_large_modal = WebElement(driver, '#closeLargeModal')

