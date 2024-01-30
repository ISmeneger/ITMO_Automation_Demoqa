import time
from pages.tables import Tables


# Задача 1
def test_add_button_form(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    page_tables.btn_add.click()
    assert page_tables.reg_form.exist()

    page_tables.btn_submit.click()
    assert page_tables.reg_form.exist()
    time.sleep(2)

    page_tables.first_name_field.send_keys('Ilya')
    page_tables.last_name_field.send_keys('S')
    page_tables.email_field.send_keys('email@yandex.ru')
    page_tables.age_field.send_keys('38')
    page_tables.salary_field.send_keys('150000')
    page_tables.department_field.send_keys('Engineering')
    page_tables.btn_submit.click()
    time.sleep(2)
    assert page_tables.string_exist.get_text() == 'Ilya'

    page_tables.edit_record.click()
    page_tables.first_name_field.clear()
    page_tables.first_name_field.send_keys('Alexander')
    page_tables.btn_submit.click()
    time.sleep(2)
    assert page_tables.string_exist.get_text() == 'Alexander'
    time.sleep(2)

    page_tables.delete_record.click()
    assert page_tables.string_exist.get_text() == ' '
    time.sleep(2)

# Задача 2
def test_next_previous_buttons(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    page_tables.select_row.scroll_to_element()
    page_tables.select_row.click()
    page_tables.establish_5row.click()
    time.sleep(2)

    for i in range(3):
        page_tables.btn_add.click()
        page_tables.first_name_field.send_keys('Ilya')
        page_tables.last_name_field.send_keys('S')
        page_tables.email_field.send_keys('email@yandex.ru')
        page_tables.age_field.send_keys('38')
        page_tables.salary_field.send_keys('150000')
        page_tables.department_field.send_keys('Engineering')
        page_tables.btn_submit.click()
        time.sleep(3)

    assert page_tables.string_exist.get_text() == 'Ilya'

    page_tables.btn_next.click()
    time.sleep(2)

    assert page_tables.page_num.get_dom_attribute('value') == '2'

    page_tables.btn_previous.click()
    time.sleep(2)

    assert page_tables.page_num.get_dom_attribute('value') == '1'

