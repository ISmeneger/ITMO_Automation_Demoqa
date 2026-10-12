import pytest
from selenium.common.exceptions import TimeoutException
from pages.form_page import FormPage


@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason='DemoQA: Close leaves the submitted form modal open (local run 2026-10-13)')
def test_close_submitted_form(browser):
    page = FormPage(browser)
    page.visit()
    page.first_name.send_keys('Tester')
    page.last_name.send_keys('Example')
    page.gender_radio_1.click_force()
    page.user_number.send_keys('9992223344')
    page.btn_submit.click()
    page.modal_dialog.wait_visible()
    page.btn_close_modal.click()
    try:
        page.modal_dialog.wait_hidden()
    except TimeoutException:
        assert not page.modal_dialog.visible(), 'Close button did not dismiss the submitted form modal'
