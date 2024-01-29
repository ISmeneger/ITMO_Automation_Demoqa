from pages.base_page import BasePage
from components.components import WebElement
class KoupAdd(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)

        self.btn_add= WebElement(driver, 'div > button')
        self.btns_delete= WebElement(driver, '#elements > button')
