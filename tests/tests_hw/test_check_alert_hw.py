from pages.alerts import Alerts


# Задача 2.
def test_check_alert(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()

    page_alerts.timer_alert_button.click()

    assert page_alerts.wait_alert()

    page_alerts.wait_alert().accept()
    assert not page_alerts.alert()


