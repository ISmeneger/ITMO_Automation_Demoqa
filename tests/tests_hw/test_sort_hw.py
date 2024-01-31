import time
from pages.tables import Tables


# Задача 3.
def test_sort(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    # Кликаем на заголовок первого столбца "First Name" для сортировки по возратанию
    page_tables.first_name_column.click()
    time.sleep(2)

    # Проверка сортировки по возратанию
    assert page_tables.first_name_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    # Кликаем на заголовок первого столбца "First Name" для сортировки по убыванию
    page_tables.first_name_column.click()
    time.sleep(2)

    # Проверка сортировки по убыванию
    assert page_tables.first_name_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'
    time.sleep(2)

    page_tables.last_name_column.click()
    time.sleep(2)

    assert page_tables.last_name_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.last_name_column.click()
    time.sleep(2)

    assert page_tables.last_name_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    page_tables.age_column.click()
    time.sleep(2)

    assert page_tables.age_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.age_column.click()
    time.sleep(2)

    assert page_tables.age_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    page_tables.email_column.click()
    time.sleep(2)

    assert page_tables.email_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.email_column.click()
    time.sleep(2)

    assert page_tables.email_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    page_tables.salary_column.click()
    time.sleep(2)

    assert page_tables.salary_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.salary_column.click()
    time.sleep(2)

    assert page_tables.salary_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    page_tables.department_column.click()
    time.sleep(2)

    assert page_tables.department_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.department_column.click()
    time.sleep(2)

    assert page_tables.department_column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'