import logging
from conftest import testdata
from testpage import OperationHelper


def test_step1(browser):
    logging.info("Test 1 Starting")
    testpag = OperationHelper(browser)
    testpag.go_to_site()
    testpag.enter_login(testdata['username'])
    testpag.enter_pass(testdata['password'])
    testpag.click_login_button()
    assert testpag.check_login_success(), "Login failed"
    testpag.create_post(testdata['title'], testdata['content'])
    testpag.test_contact_us()