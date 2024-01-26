import time
from pages.text_box import TextBox


def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('Ilya S')
    text_box.current_address.send_keys('Russia, Saint Petersburg')
    text_box.btn_submit.click_force()
    assert text_box.text_appear.exist()


