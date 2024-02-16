from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class WebElement:

    def __init__(self, driver, locator='', locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    # Поиск элемента
    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    # Поиск элементов (по неуникальному локатору) (проверка равенства кол-ва элементов, проверка неравенства кол-ва элементов)
    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    # Кликнуть на элемент
    def click(self):
        self.find_element().click()

    # Кликнуть на элемент принудительно
    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    # Получить текст элемента
    def get_text(self):
        return str(self.find_element().text)

    # Элемент есть в DOM (not exist - элемента нет в DOM)
    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    # Элемент виден на странице (not visible - элемент НЕ виден на странице)
    def visible(self):
        return self.find_element().is_displayed()

    #
    def check_count_elements(self, count: int):
        if len(self.find_elements()) == count:
            return True
        return False

    # Ввести текст
    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    # Очищает текстовое поле
    def clear(self):
        self.send_keys(Keys.CONTROL + 'a')
        self.send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def check_css(self, style, value=''):
        return self.find_element().value_of_css_property(style) == value

    def scroll_to_element(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);",
        self.find_element()
        )

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('Locator type ' + self.locator_type + ' not correct')
        return False


