from testpage import OperationsHelper
import logging
import yaml

with open('testdata.yaml') as f:
    data = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401", "Test 1 FAIL"


def test_step2(browser):
    logging.info("Test 2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(data["user"])
    testpage.enter_pass(data["user_pass"])
    testpage.click_login_button()
    testpage.short_pause()
    assert testpage.login_success() == f"Hello, {data['user']}", "Test 2 FAIL"


def test_step3(browser):
    logging.info("Test 3 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_plus_post_button()
    testpage.input_title("For Emperor!")
    testpage.input_description("Glory to the Emperor!")
    testpage.input_content("My God is the Emperor!")
    testpage.click_save_button()
    testpage.short_pause()
    assert testpage.post_success() == "For Emperor!", "Test 3 FAIL"


def test_step4(browser):
    logging.info("Test 4 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_delete_btn()
    assert "For Emperor!" not in testpage.success_delete(), "Test 4 FAIL"


def test_step5(browser):
    logging.info("Test 5 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_contact_btn()
    testpage.input_name("Lexa")
    testpage.input_mail("revus1337@gmail.com")
    testpage.input_contact_content("Возьмите на работу автотестером, пожожда!")
    testpage.click_contact_us_btn()
    testpage.short_pause()
    assert testpage.alert() == "Form successfully submitted", "Test 5 FAIL"
