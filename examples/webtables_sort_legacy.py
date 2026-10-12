import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.tables import Tables


@pytest.mark.regress
@pytest.mark.parametrize('index,numeric', [(0, False), (1, False), (2, True),
                                           (3, False), (4, True), (5, False)])
def test_sort(browser, index, numeric):
    page = Tables(browser)
    page.visit()
    headers = browser.find_elements(By.CSS_SELECTOR, '.rt-thead.-header .rt-th')

    def values():
        result = []
        for row in browser.find_elements(By.CSS_SELECTOR, '.rt-tbody .rt-tr'):
            cells = row.find_elements(By.CSS_SELECTOR, '.rt-td')
            if cells and cells[0].text.strip():
                text = cells[index].text.strip()
                result.append(int(text) if numeric else text.lower())
        return result

    assert len(values()) > 1
    for descending in (False, True):
        headers[index].click()
        WebDriverWait(browser, 10).until(
            lambda _: ('-sort-desc' if descending else '-sort-asc')
            in headers[index].get_attribute('class'))
        WebDriverWait(browser, 10).until(
            lambda _: values() == sorted(values(), reverse=descending))
        assert values() == sorted(values(), reverse=descending)
