from pages.alerts import Alerts


def test_alert(browser):
    """Проверка видимости алерта"""
    page_alerts = Alerts(browser)
    page_alerts.visit()

    assert not page_alerts.alert()

    page_alerts.alert_button.click()


    assert page_alerts.wait_alert()
    page_alerts.wait_alert().accept()


def test_alert_text(browser):
    """Подтверждение текста алерта"""
    page_alerts = Alerts(browser)
    page_alerts.visit()

    page_alerts.alert_button.click()


    assert "You clicked a button" == page_alerts.wait_alert().text
    page_alerts.wait_alert().accept()

    assert not page_alerts.alert()


def test_confirm(browser):
    """Отмена алерта"""
    page_alerts = Alerts(browser)
    page_alerts.visit()

    page_alerts.confirm_button.click()

    page_alerts.wait_alert().dismiss()

    assert page_alerts.confirm_result.get_text() == 'You selected Cancel'


def test_prompt(browser):
    """Проверка ввода текста в алерт"""
    page_alerts = Alerts(browser)
    page_alerts.visit()
    name = 'Ilya'

    page_alerts.promt_button.click()


    page_alerts.wait_alert().send_keys(name)
    page_alerts.wait_alert().accept()

    assert page_alerts.prompt_result.get_text() == f'You entered {name}'


