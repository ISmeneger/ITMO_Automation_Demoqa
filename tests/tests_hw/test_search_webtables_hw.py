import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.tables import Tables


@pytest.mark.regress
@pytest.mark.parametrize('column,query', [(0, 'Cierra'), (1, 'Cantrell'), (2, '39'),
                                          (3, 'kierra@example.com'), (4, '12000'), (5, 'Legal')])
def test_search_table(browser, column, query):
    page = Tables(browser)
    page.visit()
    initial_count = len(page.rows())
    page.search.send_keys(query)
    WebDriverWait(browser, 10).until(lambda _: bool(page.rows()) and
        all(query.lower() in row[column].lower() for row in page.rows()))
    assert len(page.rows()) == 1
    assert query.lower() in page.rows()[0][column].lower()
    page.search.clear()
    WebDriverWait(browser, 10).until(lambda _: len(page.rows()) == initial_count)
    assert len(page.rows()) == initial_count
