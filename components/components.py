from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class WebElement:

    def __init__(self, driver, locator='', locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    # Метод для поиска элемента
    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    # Метод для поиска элементов (по неуникальному локатору) (проверка равенства кол-ва элементов, проверка неравенства кол-ва элементов)
    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    # Метод, позволяющий кликнуть на элемент
    def click(self):
        self.find_element().click()

    # Метод, позволяющий кликнуть на элемент принудительно
    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    # Метод для получения текста элемента
    def get_text(self):
        return str(self.find_element().text)

    # Метод для проверки существования элемента в DOM (not exist - элемента нет в DOM)
    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    # Метод проверки видимости элемнта на странице (not visible - элемент НЕ виден на странице)
    def visible(self):
        return self.find_element().is_displayed()

    # Метод для проверки кол-ва одинаковых элементов на странице
    def check_count_elements(self, count: int):
        if len(self.find_elements()) == count:
            return True
        return False

    # Метод для ввода текста
    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    # Метод для очистки текстового поля
    def clear(self):
        self.send_keys(Keys.CONTROL + 'a')
        self.send_keys(Keys.DELETE)

    # Метод, который возвращает значение атрибутов с заданным именем
    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    # Метод для проверки стилей CSS
    def check_css(self, style, value=''):
        return self.find_element().value_of_css_property(style) == value

    # Метод прокрутки страницы до любого элемента
    def scroll_to_element(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);",
        self.find_element()
        )

    # Метод для работы с любым типом локатора
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


