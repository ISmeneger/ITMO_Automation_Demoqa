import logging
from components.components import WebElement


class BasePage:
    def __init__(self, driver, base_url):
        self.last_name_field = None
        self.driver = driver
        self.base_url = base_url
        self.viewport = WebElement(driver, 'head > meta:nth-child(2)')

    # Метод входа на страницу
    def visit(self):
        return self.driver.get(self.base_url)

    # .current_url - получить текущий URL
    def get_url(self):
        return self.driver.current_url

    # Метод проверки URL
    def equal_url(self) -> object:
        if self.get_url() == self.base_url:
            return True
        return False

    # .back() - стрелка назад в браузере
    def back(self):
        self.driver.back()

    # .forward() - стрелка вперед в браузере
    def forward(self):
        self.driver.forward()

    # .refresh() - обновить страницу
    def refresh(self):
        self.driver.refresh()

    # .title - получить title страницы
    def get_title(self):
        return self.driver.title

    # Метод alert (такой метод позволяет нам проверить открыт ли алерт и дает возможность работать
    # с окном, но не позволяет проверить, что окно НЕ открыто)
    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False








