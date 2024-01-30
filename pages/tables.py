from pages.base_page import BasePage
from components.components import WebElement

class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables '
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, '//*[contains(@id, "delete")]', 'xpath')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.reg_form = WebElement(driver, 'div.fade.modal.show > div > div')
        self.btn_submit = WebElement(driver, '#submit')
        self.first_name_field = WebElement(driver, '#firstName')
        self.last_name_field = WebElement(driver, '#lastName')
        self.email_field = WebElement(driver, '#userEmail')
        self.age_field = WebElement(driver, '#age')
        self.salary_field = WebElement(driver, '#salary')
        self.department_field = WebElement(driver, '#department')

        self.string_exist = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(1)')
        self.edit_record = WebElement(driver, '#edit-record-4')
        self.delete_record = WebElement(driver, '#delete-record-4')

        self.select_row = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.establish_5row = WebElement(driver, 'select > option:nth-child(1)')
        self.btn_next = WebElement(driver, 'div.-next > button')
        self.page_num = WebElement(driver,'div > input[type=number]')
        self.btn_previous = WebElement(driver,'div.-previous > button')












