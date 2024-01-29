import time
from pages.tables import Tables


# def test_tables(browser):
#     """Проверка блока кода No rows found """
#     page_tables = Tables(browser)
#
#     page_tables.visit()
#     assert not page_tables.no_data.exist()
#
#     """Удаляем все записи"""
#     while page_tables.btn_delete_row.exist():
#         page_tables.btn_delete_row.click()
#
#     time.sleep(2)
#     assert page_tables.no_data.exist()

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
    assert page_tables.string_exsist.get_text() == 'Ilya'

    page_tables.edit_record.click()
    page_tables.first_name_field.clear()
    page_tables.first_name_field.send_keys('Alexander')
    page_tables.btn_submit.click()
    time.sleep(2)
    assert page_tables.string_exsist.get_text() == 'Alexander'
    time.sleep(2)

    page_tables.delete_record.click()
    assert page_tables.string_exsist.get_text() == ' '
    time.sleep(2)

# Задача 2















