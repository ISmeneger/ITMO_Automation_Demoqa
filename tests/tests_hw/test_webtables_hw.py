from selenium.webdriver.support.ui import WebDriverWait
from pages.tables import Tables


def test_add_button_form(browser):
    page = Tables(browser)
    page.visit()
    page.btn_add.click()
    page.reg_form.wait_visible()
    page.btn_submit.click()
    assert page.reg_form.visible()
    assert browser.execute_script('return arguments[0].validity.valueMissing',
                                  page.first_name_field.find_element())
    page.fill_record('Ilya')
    WebDriverWait(browser, 10).until(lambda _: any(row[0] == 'Ilya' for row in page.rows()))
    assert ['Ilya', 'Tester', '38', 'qa@example.com', '150000', 'Engineering'] in page.rows()
    page.action_for('Ilya', 'Edit')
    page.fill_record('Alexander')
    assert any(row[0] == 'Alexander' for row in page.rows())
    assert not any(row[0] == 'Ilya' for row in page.rows())
    page.action_for('Alexander', 'Delete')
    WebDriverWait(browser, 10).until(lambda _: not any(row[0] == 'Alexander' for row in page.rows()))
    assert len(page.rows()) == 3


def test_next_previous_buttons(browser):
    page = Tables(browser)
    page.visit()
    page.select_page_size(10)
    for i in range(8):
        page.add_record(f'Pagination{i}', email=f'pagination{i}@example.com')
    assert len(page.rows()) == 10
    assert page.page_num.get_text() == '1 of 2'
    page.btn_next.click()
    WebDriverWait(browser, 10).until(lambda _: page.page_num.get_text() == '2 of 2')
    assert len(page.rows()) == 1
    assert page.rows()[0][0] == 'Pagination7'
    page.btn_previous.click()
    WebDriverWait(browser, 10).until(lambda _: page.page_num.get_text() == '1 of 2')
    assert len(page.rows()) == 10
