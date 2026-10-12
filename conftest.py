from pathlib import Path
import re
import os

import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    """Each test gets its own browser, tabs and page state."""
    options = webdriver.ChromeOptions()
    if os.getenv('HEADLESS', '').lower() in {'1', 'true', 'yes'}:
        options.add_argument('--headless=new')
    options.add_argument('--window-size=1280,1000')
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    try:
        yield driver
    finally:
        driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != 'call' or not report.failed:
        return
    driver = item.funcargs.get('browser')
    if driver is None:
        return
    folder = Path('artifacts')
    folder.mkdir(exist_ok=True)
    name = re.sub(r'[^A-Za-z0-9_.-]', '_', item.nodeid)
    try:
        driver.save_screenshot(str(folder / f'{name}.png'))
        (folder / f'{name}.html').write_text(driver.page_source, encoding='utf-8')
        (folder / f'{name}.txt').write_text(driver.current_url, encoding='utf-8')
    except Exception as error:
        # Diagnostic collection must not replace the original test failure.
        item.warn(pytest.PytestWarning(f'Could not collect browser diagnostics: {error}'))
