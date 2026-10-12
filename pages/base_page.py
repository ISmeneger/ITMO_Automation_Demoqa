from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from components.components import WebElement


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.viewport = WebElement(driver, 'head > meta[name=viewport]')

    def visit(self):
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script('return document.readyState') == 'complete')
        if 'demoqa.com' in self.base_url:
            WebDriverWait(self.driver, 10).until(
                lambda d: d.find_elements('css selector', '#root header'))

    # перейти по урлу
    def get_url(self):
        return self.driver.current_url

    # .current_url - получить текущий URL
    def equal_url(self) -> bool:
        return self.get_url().rstrip('/') == self.base_url.rstrip('/')

    # .back() - стрелка назад в браузере
    def back(self):
        self.driver.back()

    # forward() - стрелка вперед в браузере
    def forward(self):
        self.driver.forward()

    # .refresh() - обновить страницу
    def refresh(self):
        self.driver.refresh()

    # .title - получить title страницы
    def get_title(self):
        return self.driver.title

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except NoAlertPresentException:
            return False


    def wait_alert(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())

    def wait_url(self):
        return WebDriverWait(self.driver, 10).until(
            lambda _: self.equal_url())
