from unittest.mock import Mock

import pytest
from selenium.common.exceptions import NoAlertPresentException, WebDriverException

from components.components import WebElement
from pages.base_page import BasePage


def test_input_value_uses_property_instead_of_text():
    native = Mock(text='')
    native.get_property.return_value = 'still-filled'
    driver = Mock()
    driver.find_element.return_value = native
    assert WebElement(driver, '#input').get_value() == 'still-filled'
    native.get_property.assert_called_once_with('value')


def test_empty_boolean_attribute_is_preserved():
    native = Mock()
    native.get_dom_attribute.return_value = ''
    driver = Mock()
    driver.find_element.return_value = native
    assert WebElement(driver, '#input').get_dom_attribute('required') == ''


def test_scroll_uses_the_requested_element():
    native = Mock()
    driver = Mock()
    driver.find_element.return_value = native
    WebElement(driver, '#target').scroll_to_element()
    script, argument = driver.execute_script.call_args.args
    assert 'scrollIntoView' in script
    assert argument is native


def test_invalid_locator_is_rejected():
    with pytest.raises(ValueError, match='Unknown locator'):
        WebElement(Mock(), '#input', 'unsupported').get_by_type()


def test_absent_alert_is_reported():
    driver = Mock()
    type(driver.switch_to).alert = property(
        lambda self: (_ for _ in ()).throw(NoAlertPresentException()))
    assert BasePage(driver, 'https://example.test').alert() is False


def test_driver_errors_are_not_hidden_as_missing_alert():
    driver = Mock()
    type(driver.switch_to).alert = property(
        lambda self: (_ for _ in ()).throw(WebDriverException('disconnected')))
    with pytest.raises(WebDriverException, match='disconnected'):
        BasePage(driver, 'https://example.test').alert()


def test_react_input_clear_uses_keyboard_deletion():
    from selenium.webdriver.common.keys import Keys
    native = Mock()
    native.get_property.return_value = ''
    native.is_displayed.return_value = True
    native.is_enabled.return_value = True
    driver = Mock(capabilities={'platformName': 'windows'})
    driver.find_element.return_value = native
    WebElement(driver, '#searchBox').clear()
    assert native.send_keys.call_args_list[0].args == (Keys.CONTROL, 'a')
    assert native.send_keys.call_args_list[1].args == (Keys.BACKSPACE,)
    native.clear.assert_not_called()


def test_footer_interception_can_activate_native_button_with_keyboard():
    from selenium.common.exceptions import ElementClickInterceptedException
    from selenium.webdriver.common.keys import Keys
    native = Mock(tag_name='button')
    native.click.side_effect = ElementClickInterceptedException(
        'Other element would receive the click: <footer>')
    native.is_displayed.return_value = True
    native.is_enabled.return_value = True
    driver = Mock()
    driver.find_element.return_value = native
    WebElement(driver, '#submit').click()
    native.send_keys.assert_called_once_with(Keys.ENTER)


def test_unrelated_click_interception_is_not_hidden():
    from selenium.common.exceptions import ElementClickInterceptedException
    native = Mock(tag_name='button')
    native.click.side_effect = ElementClickInterceptedException(
        'Other element would receive the click: <div class="modal">')
    native.is_displayed.return_value = True
    native.is_enabled.return_value = True
    driver = Mock()
    driver.find_element.return_value = native
    with pytest.raises(ElementClickInterceptedException):
        WebElement(driver, '#submit').click()
    native.send_keys.assert_not_called()


def test_footer_does_not_trigger_keyboard_fallback_for_non_native_control():
    from selenium.common.exceptions import ElementClickInterceptedException
    native = Mock(tag_name='span')
    native.click.side_effect = ElementClickInterceptedException(
        'Other element would receive the click: <footer>')
    native.is_displayed.return_value = True
    native.is_enabled.return_value = True
    driver = Mock()
    driver.find_element.return_value = native
    with pytest.raises(ElementClickInterceptedException):
        WebElement(driver, '#delete').click()
    native.send_keys.assert_not_called()
