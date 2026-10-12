from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/webtables')
        self.btn_delete_row = WebElement(driver, '[id^="delete-record-"]')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.reg_form = WebElement(driver, '.modal.show .modal-content')
        self.btn_submit = WebElement(driver, '#userForm #submit')
        self.first_name_field = WebElement(driver, '#firstName')
        self.last_name_field = WebElement(driver, '#lastName')
        self.email_field = WebElement(driver, '#userEmail')
        self.age_field = WebElement(driver, '#age')
        self.salary_field = WebElement(driver, '#salary')
        self.department_field = WebElement(driver, '#department')
        self.search = WebElement(driver, '#searchBox')
        self.select_row = WebElement(driver, '.web-tables-wrapper .pagination select')
        self.btn_next = WebElement(driver, '//div[contains(@class,"pagination")]//button[normalize-space()="Next"]', 'xpath')
        self.btn_previous = WebElement(driver, '//div[contains(@class,"pagination")]//button[normalize-space()="Previous"]', 'xpath')
        self.page_num = WebElement(driver, '.web-tables-wrapper .pagination strong')

    def visit(self):
        super().visit()
        self.btn_add.wait_visible()
        WebDriverWait(self.driver, 10).until(lambda _: len(self.rows()) == 3)

    def rows(self):
        return [[cell.text for cell in row.find_elements(By.CSS_SELECTOR, 'td')[:6]]
                for row in self.driver.find_elements(By.CSS_SELECTOR, '.web-tables-wrapper tbody tr')]

    def fill_record(self, first_name, last_name='Tester', email='qa@example.com',
                    age='38', salary='150000', department='Engineering'):
        self.reg_form.wait_visible()
        for field, value in [(self.first_name_field, first_name),
                             (self.last_name_field, last_name), (self.email_field, email),
                             (self.age_field, age), (self.salary_field, salary),
                             (self.department_field, department)]:
            field.clear()
            field.send_keys(value)
        self.btn_submit.click()
        self.reg_form.wait_hidden()

    def add_record(self, first_name, **kwargs):
        self.btn_add.click()
        self.fill_record(first_name, **kwargs)

    def action_for(self, first_name, action):
        # Test names are controlled data; locate by row content, never row index.
        row = WebDriverWait(self.driver, 10).until(lambda _: next(
            (row for row in self.driver.find_elements(By.CSS_SELECTOR, '.web-tables-wrapper tbody tr')
             if row.find_elements(By.CSS_SELECTOR, 'td')[0].text == first_name), None))
        row.find_element(By.CSS_SELECTOR, f'span[title="{action}"]').click()

    def select_page_size(self, size):
        Select(self.select_row.wait_visible()).select_by_value(str(size))
