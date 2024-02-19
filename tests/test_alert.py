import time
from pages.alerts import Alerts


def test_alert(browser):
    """Проверка видимости алерта"""
    page_alerts = Alerts(browser)
    page_alerts.visit()

    assert not page_alerts.alert()

    page_alerts.alert_button.click()
    time.sleep(2)

    assert page_alerts.alert()


def test_alert_text(browser):
    """Подтверждение текста алерта"""
    page_alerts = Alerts(browser)
    page_alerts.visit()

    page_alerts.alert_button.click()
    time.sleep(2)

    assert "You clicked a button" == page_alerts.alert().text
    page_alerts.alert().accept()

    assert not page_alerts.alert()


def test_confirm(browser):
    """Отмена алерта"""
    page_alerts = Alerts(browser)
    page_alerts.visit()

    page_alerts.confirm_button.click()
    time.sleep(2)
    page_alerts.alert().dismiss()

    assert page_alerts.confirm_result.get_text() == 'You selected Cancel'


def test_prompt(browser):
    """Проверка ввода текста в алерт"""
    page_alerts = Alerts(browser)
    page_alerts.visit()
    name = 'Ilya'

    page_alerts.promt_button.click()
    time.sleep(2)

    page_alerts.alert().send_keys(name)
    page_alerts.alert().accept()

    assert page_alerts.prompt_result.get_text() == f'You entered {name}'












