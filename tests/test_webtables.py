import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.tables import Tables


class RestoredDeletedRecordError(AssertionError):
    """The website restored a record already removed in this scenario."""


@pytest.mark.xfail(
    strict=True,
    raises=RestoredDeletedRecordError,
    reason='DemoQA Web Tables: consecutive deletion can restore earlier records; stale initial state in memoized cells',
)
def test_tables(browser):
    page = Tables(browser)
    page.visit()
    initial_rows = page.rows()
    if len(initial_rows) != 3:
        raise ValueError(f'Expected three initial records, got {initial_rows!r}')
    deleted_names = set()
    for remaining in (2, 1, 0):
        before = page.rows()
        target_name = before[0][0]
        page.action_for(target_name, 'Delete')
        WebDriverWait(browser, 10).until(
            lambda _: target_name not in {row[0] for row in page.rows()})
        deleted_names.add(target_name)
        rows = page.rows()
        restored = deleted_names.intersection(row[0] for row in rows)
        if restored:
            raise RestoredDeletedRecordError(
                f'Previously deleted records restored: {sorted(restored)!r}; '
                f'current rows: {rows!r}')
        assert len(rows) == remaining
    assert page.rows() == []
    assert not page.btn_delete_row.exist()
