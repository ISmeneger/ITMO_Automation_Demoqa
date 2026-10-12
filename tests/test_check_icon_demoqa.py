from pages.demoqa import DemoQa
def test_check_icon(browser):

    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    demo_qa_page.icon.click()
    assert demo_qa_page.wait_url()

    assert demo_qa_page.icon.exist()