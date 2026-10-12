from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WebElement:
    """Reusable element actions with bounded explicit waits."""

    LOCATOR_TYPES = {
        "id": By.ID, "name": By.NAME, "xpath": By.XPATH,
        "css": By.CSS_SELECTOR, "class": By.CLASS_NAME, "link": By.LINK_TEXT,
    }

    def __init__(self, driver, locator='', locator_type='css', timeout=10):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type
        self.timeout = timeout

    def get_by_type(self):
        if self.locator_type not in self.LOCATOR_TYPES:
            raise ValueError(f"Unknown locator type: {self.locator_type}")
        return self.LOCATOR_TYPES[self.locator_type]

    @property
    def by(self):
        return self.get_by_type(), self.locator

    def find_element(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.by))

    def find_elements(self):
        return self.driver.find_elements(*self.by)

    def click(self):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.by))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except ElementClickInterceptedException as error:
            # DemoQA's fixed footer overlaps bottom buttons. Activate only
            # native keyboard-accessible controls, without hiding the footer.
            if '<footer' not in error.msg or element.tag_name.lower() not in {'button', 'a'}:
                raise
            element.send_keys(Keys.ENTER)

    def click_force(self):
        # DemoQA has hidden native radio/checkbox inputs with custom labels.
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def get_text(self):
        return self.wait_visible().text

    def get_value(self):
        return self.find_element().get_property('value')

    def exist(self):
        return bool(self.find_elements())

    def visible(self):
        return any(element.is_displayed() for element in self.find_elements())

    def wait_visible(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.by))

    def wait_hidden(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located(self.by))

    def check_count_elements(self, count):
        return len(self.find_elements()) == count

    def send_keys(self, text):
        self.wait_visible().send_keys(text)

    def clear(self):
        element = self.wait_visible()
        platform = self.driver.capabilities.get('platformName', '').lower()
        modifier = Keys.COMMAND if 'mac' in platform else Keys.CONTROL
        # Native clear() can empty React-controlled inputs without firing
        # the input event consumed by React. Keyboard deletion updates state.
        element.send_keys(modifier, 'a')
        element.send_keys(Keys.BACKSPACE)
        WebDriverWait(self.driver, self.timeout).until(
            lambda _: self.get_value() == '')

    def get_dom_attribute(self, name):
        return self.find_element().get_dom_attribute(name)

    def check_css(self, style, value=''):
        return self.find_element().value_of_css_property(style) == value

    def scroll_to_element(self):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", self.find_element())
