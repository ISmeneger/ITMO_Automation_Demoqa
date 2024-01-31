import time
from pages.modal_dialogs import ModalDialogs
import pytest
import requests


#  Задача 1.
def test_check_modal(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    try:
        response = requests.get('https://demoqa.com/modal-dialogs')
        response.raise_for_status()
    except requests.exceptions.RequestException:
        pytest.skip('Request failed, skip the test')

    modal_page.small_modal.click()
    time.sleep(2)
    modal_page.close_small_modal.click()
    time.sleep(2)

    modal_page.large_modal.click()
    time.sleep(2)
    modal_page.close_large_modal.click()
    time.sleep(2)



