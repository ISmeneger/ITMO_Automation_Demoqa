from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    page = ModalDialogs(browser)
    page.visit()
    page.small_modal.click()
    assert page.close_small_modal.wait_visible()
    page.close_small_modal.click()
    assert page.close_small_modal.wait_hidden()
    page.large_modal.click()
    assert page.close_large_modal.wait_visible()
    page.close_large_modal.click()
    assert page.close_large_modal.wait_hidden()
