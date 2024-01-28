import time
from pages.text_box import TextBox


def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    name = 'Ilya S'
    current_address = 'Russia, Saint Petersburg'

    text_box.name.send_keys(name)
    time.sleep(2)
    text_box.current_address.send_keys(current_address)
    time.sleep(2)
    text_box.btn_submit.click_force()
    assert text_box.text_appear.exist()
    assert text_box.text_appear.get_text() == (f'Name:{name}\n'
                                            f'Current Address :{current_address}')








