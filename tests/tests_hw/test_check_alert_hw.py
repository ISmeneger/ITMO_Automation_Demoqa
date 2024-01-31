import time
from pages.alerts import Alerts


# Задача 2.
def test_check_alert(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()

    page_alerts.timer_alert_button.click()
    time.sleep(6)
    assert page_alerts.alert()

    page_alerts.alert().accept()
    assert not page_alerts.alert()



