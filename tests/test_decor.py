from pages.demoqa import DemoQa
from pages.radio_button import RadioButton
import pytest


# Декоратор skip, который позволяет пропустить тестовую функцию
@pytest.mark.skip
def test_decor(browser):
    page_demo = DemoQa(browser)
    page_demo.visit()

    assert page_demo.h5.check_count_elements(6)

    # проверяем что есть какой-то текст в заголовках

    for element in page_demo.h5.find_elements():
        assert element.text != ''

# Декоратор skipif позволяет пропускать тест кейс исходя из условия
@pytest.mark.skipif(True, reason='просто пропуск')
def test_decor_2(browser):
    page_radio = RadioButton(browser)
    page_radio.visit()

    page_radio.yes_radio.click_force()
    assert page_radio.text.get_text() == 'You have selected Yes'

    page_radio.impressive_radio.click_force()
    assert page_radio.text.get_text() == 'You have selected Impressive'

    assert 'disabled' in page_radio.no_radio.get_dom_attribute('class')

