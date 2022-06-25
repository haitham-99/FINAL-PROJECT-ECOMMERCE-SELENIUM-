import time
import pytest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = r".\drivers\chromedriver.exe"
    chrome_options = ChromeOptions()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS "
                                "X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                                "Version/14.0.3 Mobile/15E148 Safari/604.1")

    ser_chrome = ChromeService(chrome_driver)
    driver = webdriver.Chrome(service=ser_chrome, options=chrome_options)
    # ipad mini
    driver.set_window_size(768, 1024)
    yield driver
    driver.close()


def test_user_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(4)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(2)
    driver.find_element(By.ID, "login-firstname").send_keys("at")
    time.sleep(2)
    driver.find_element(By.ID, "login-lastname").send_keys("tes")
    time.sleep(2)
    gender_radio = driver.find_element(By.CSS_SELECTOR, ".gl-radio-input__option:nth-child(1) > .gl-radio-input__label")
    driver.execute_script("arguments[0].click();", gender_radio)
    time.sleep(2)
    driver.find_element(By.ID, "login-email").send_keys("b_test_pytest@gmail.com")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#login-password").send_keys("Hh123456789+")
    time.sleep(2)
    age_check = driver.find_element(By.NAME, "age")
    driver.execute_script("arguments[0].click();", age_check)
    time.sleep(2)
    member_check = driver.find_element(By.NAME, "doc-tnc-memb")
    driver.execute_script("arguments[0].click();", member_check)
    time.sleep(2)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(3)
    actualUrl = driver.current_url
    assert actualUrl == "https://www.adidas.co.il/en/account"


def test_user_signin_successfully(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "#login-email").send_keys("haithamodeh57@gmail.com")
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "#login-password").send_keys("Hh123456789+")
    time.sleep(4)
    element = driver.find_element(By.CSS_SELECTOR, "#ok")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(4)
    actualUrl = driver.current_url
    assert actualUrl == "https://www.adidas.co.il/en/account"


# Negative Scenarios
def test_user_signin_email_err(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#login-email").send_keys("haitham1odeh57@gmail.com.")
    element = driver.find_element(By.CSS_SELECTOR, "#ok")
    driver.execute_script("arguments[0].click();", element)
    err_email_message = driver.find_element(By.CSS_SELECTOR,
                                            "#form > div.d-flex.justify-content-center.account-login > div:nth-child("
                                            "1) > div > div > div.gl-vspace > div > div > div").text
    assert err_email_message == "Please enter a valid e-mail address"


def test_first_name_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(2)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    err_firstname_message = driver.find_element(By.CSS_SELECTOR,
                                                "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(7) > div > div").text
    assert err_firstname_message == "Please enter a valid first name"


def test_last_name_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(2)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    err_lastname_message = driver.find_element(By.CSS_SELECTOR,
                                               "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(9) > div > div").text
    assert err_lastname_message == "Please enter a valid last name"


def test_gender_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(2)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    err_gender_message = driver.find_element(By.CSS_SELECTOR,
                                             "#gender-hint--error").text
    assert err_gender_message == "Please select gender"


def test_email_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(2)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    err_email_message = driver.find_element(By.CSS_SELECTOR,
                                            "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div.gl-vspace > div > div > div").text
    assert err_email_message == "Please enter a valid e-mail address"


def test_password_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(2)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    err_password_message = driver.find_element(By.CSS_SELECTOR,
                                               "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(16) > div > div > div > div > div.gl-form-hint.gl-form-hint--error.gl-form-hint--error--show").text
    assert err_password_message == "Please enter your password"


def test_confirm_age_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(2)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    err_confirm_age_message = driver.find_element(By.CSS_SELECTOR,
                                                  "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div.gl-checkbox.gl-form-item--required.gl-form-item--error > div").text
    assert err_confirm_age_message == "Please confirm your age"


def test_x_icon_first_name_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(2)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(3)
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(7) > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#cross-small"


def test_v_icon_first_name_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(3)
    driver.find_element(By.ID, "login-firstname").send_keys("hi")
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(7) > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#checkbox-checkmark"


def test_x_icon_second_name_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(2)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(3)
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(9) > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#cross-small"


def test_v_icon_second_name_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(3)
    driver.find_element(By.ID, "login-lastname").send_keys("hi")
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(9) > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#checkbox-checkmark"


def test_x_icon_email_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(3)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(3)
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div.gl-vspace > div > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#cross-small"


def test_v_icon_email_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(3)
    driver.find_element(By.ID, "login-email").send_keys("h@h.com")
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div.gl-vspace > div > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#checkbox-checkmark"


def test_x_icon_password_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(3)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(3)
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(16) > div > div > div > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#cross-small"


def test_v_icon_password_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(3)
    driver.find_element(By.ID, "login-password").send_keys("Aa123456+")
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(16) > div > div > div > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#checkbox-checkmark"


def test_incorrect_input_first_name_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(3)
    driver.find_element(By.ID, "login-firstname").send_keys("11223344")
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(3)
    err_firstname_message = EC.visibility_of((By.XPATH, "//*[@id=\"form\"]/div[1]/div[1]/div/div/div[5]/div/div"))
    assert bool(err_firstname_message) is True


def test_incorrect_input_last_name_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(3)
    driver.find_element(By.ID, "login-lastname").send_keys("3344")
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(3)
    err_secondname_message = EC.visibility_of((By.XPATH, "//*[@id=\"form\"]/div[1]/div[1]/div/div/div[7]/div/div"))
    assert bool(err_secondname_message) is True


def test_incorrect_input_email_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(3)
    driver.find_element(By.ID, "login-email").send_keys("wwwww33@44.")
    time.sleep(2)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(2)
    err_email_message = EC.visibility_of((By.XPATH, "//*[@id=\"form\"]/div[1]/div[1]/div/div/div[11]/div/div/div"))
    assert bool(err_email_message) is True


def test_incorrect_input_password_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR,
                               "#form > div.d-flex.justify-content-center.account-login > div:nth-child(1) > div > div > div.gl-vspace-bpall-small.gl-mobile > span > a > span")
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(3)
    driver.find_element(By.ID, "login-password").send_keys("wwwww33")
    time.sleep(2)
    register_button = driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content")
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(2)
    err_password_message = EC.visibility_of(
        (By.XPATH, "//*[@id=\"form\"]/div[1]/div[1]/div/div/div[13]/div/div/div/div/div[2]"))
    assert bool(err_password_message) is True


# Automate 'Search Product' feature
def test_search_product_feature(driver):
    driver.get("https://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#sg-navbar-collapse > .navbar #women").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Clothing").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "T-Shirts & Tops").click()
    time.sleep(2)
    product_name = driver.find_element(By.XPATH,
                                       "//*[@id=\"product-search-results\"]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/a").text
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".search_icon_wrapper > img").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".search_form_wrapper .form-control").send_keys(
        "CROP TEE WITH BINDING DETAILS")
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".search_form_wrapper .form-control").send_keys(Keys.ENTER)
    time.sleep(2)
    product_search_name = driver.find_element(By.XPATH,
                                              "//*[@id=\"product-search-results\"]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/a").text
    assert product_name == product_search_name


# Automate 'Buy Product' feature
def test_buy_product_feature_with_sign_in(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#login-email").send_keys("haithamodeh57@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#login-password").send_keys("Hh123456789+")
    time.sleep(1)
    element = driver.find_element(By.CSS_SELECTOR, "#ok")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#sg-navbar-collapse > .navbar #women").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Clothing").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "T-Shirts & Tops").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".col-6:nth-child(10) .tile-image").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".swatch-rect-carbon-\\/-white").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".size-radio:nth-child(5) .size-value").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    time.sleep(2)
    driver.get("https://www.adidas.co.il/en/cart")
    time.sleep(3)
    my_quan = Select(driver.find_element(By.XPATH, "//select[contains(@class,'quantity')]"))
    my_quan.select_by_visible_text('2')
    time.sleep(1)
    price_before_checkout = driver.find_element(By.XPATH,
                                                "//*[@id=\"maincontent\"]/div/div[4]/div[3]/div[2]/div[6]/div[5]/div[2]/p").text
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".checkout-btn").click()
    time.sleep(2)
    driver.implicitly_wait(10)
    iframe = driver.find_element(By.XPATH, "//iframe[contains(@id,'Intrnl_CO_Container')]")
    driver.switch_to.frame(iframe)
    price_after_checkout = driver.find_element(By.XPATH,
                                               "//*[@id=\"itemsTotal\"]/div[1]").text
    driver.find_element(By.XPATH, "//*[@id=\"CheckoutData_BillingFirstName\"]").click()
    driver.find_element(By.XPATH, "//*[@id=\"CheckoutData_BillingFirstName\"]").send_keys("hiiiiiiiii")
    driver.find_element(By.ID, "CheckoutData_BillingLastName").send_keys("odeh")
    driver.find_element(By.ID, "CheckoutData_Email").send_keys("haithamodeh@gmail.com")
    driver.find_element(By.ID, "CheckoutData_BillingAddress1").send_keys("taibe")
    driver.find_element(By.ID, "BillingCity").send_keys("taibe")
    driver.find_element(By.ID, "BillingZIP").send_keys("1111111")
    driver.find_element(By.ID, "CheckoutData_BillingPhone").send_keys("0544444444")
    driver.find_element(By.ID, "btnPay").click()
    time.sleep(3)
    driver.switch_to.default_content()
    assert price_before_checkout == price_after_checkout


def test_buy_product_feature_with_guest_account(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#sg-navbar-collapse > .navbar #women").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Clothing").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "T-Shirts & Tops").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".col-6:nth-child(10) .tile-image").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".swatch-rect-carbon-\\/-white").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".size-radio:nth-child(5) .size-value").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    time.sleep(2)
    driver.get("https://www.adidas.co.il/en/cart")
    time.sleep(3)
    my_quan = Select(driver.find_element(By.XPATH, "//select[contains(@class,'quantity')]"))
    my_quan.select_by_visible_text('2')
    time.sleep(1)
    price_before_checkout = driver.find_element(By.XPATH,
                                                "//*[@id=\"maincontent\"]/div/div[4]/div[3]/div[2]/div[6]/div[5]/div[2]/p").text
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".checkout-btn").click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, ".checkout-as-guest").click()
    driver.implicitly_wait(10)
    iframe = driver.find_element(By.XPATH, "//iframe[contains(@id,'Intrnl_CO_Container')]")
    driver.switch_to.frame(iframe)
    price_after_checkout = driver.find_element(By.XPATH,
                                               "//*[@id=\"itemsTotal\"]/div[1]").text
    driver.find_element(By.XPATH, "//*[@id=\"CheckoutData_BillingFirstName\"]").click()
    driver.find_element(By.XPATH, "//*[@id=\"CheckoutData_BillingFirstName\"]").send_keys("hiiiiiiiii")
    driver.find_element(By.ID, "CheckoutData_BillingLastName").send_keys("odeh")
    driver.find_element(By.ID, "CheckoutData_Email").send_keys("haithamodeh@gmail.com")
    driver.find_element(By.ID, "CheckoutData_BillingAddress1").send_keys("taibe")
    driver.find_element(By.ID, "BillingCity").send_keys("taibe")
    driver.find_element(By.ID, "BillingZIP").send_keys("1111111")
    driver.find_element(By.ID, "CheckoutData_BillingPhone").send_keys("0544444444")
    driver.find_element(By.ID, "btnPay").click()
    time.sleep(3)
    driver.switch_to.default_content()
    assert price_before_checkout == price_after_checkout


# Test Case - Verify that 'Add to Wishlist' checkout only works after login.
def test_add_to_wishlist_after_login(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#sg-navbar-collapse > .navbar #women").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Clothing").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "T-Shirts & Tops").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#product-search-results > div.row.no-gutters > div.col-sm-12.col-md-9.custom-padding > div.container.p-0 > div > div.row.product-wrapsection > div:nth-child(2) > div > div > div.image-container > a.wishlistTile > div > img.heart-empty.js-heart").click()
    time.sleep(3)
    wishlist_icon = driver.find_element(By.ID, "wishlist_count")
    driver.execute_script("arguments[0].click();", wishlist_icon)
    time.sleep(2)
    login_message_wishlist = driver.find_element(By.XPATH,
                                                 "//*[@id=\"maincontent\"]/div/div/div/div[1]/div[2]/div/div[3]/div/p").text
    assert login_message_wishlist == "Register or Log in to save the item(s) so they won't be lost."


# Verify that Total Price is reflecting correctly if user changes quantity on 'Shopping Cart Summary' Page.
def test_Total_Price_is_correct(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "MEN").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Clothing").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "T-Shirts & Tops").click()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        "//*[@id=\"product-search-results\"]/div[2]/div[2]/div[2]/div/div[1]/div[6]/div/div/div[1]/a[1]/img").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".swatch-rect-off-white").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".size-radio:nth-child(3) .size-value").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".add-to-cart > .right_arrow_main").click()
    time.sleep(2)
    driver.get("https://www.adidas.co.il/en/cart")
    time.sleep(3)
    my_quan = Select(driver.find_element(By.XPATH, "//select[contains(@class,'quantity')]"))
    my_quan.select_by_visible_text('2')
    time.sleep(2)
    two_items_price = driver.find_element(By.XPATH,"//*[@id=\"maincontent\"]/div/div[4]/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div").text
    total_price = driver.find_element(By.XPATH,"//*[@id=\"maincontent\"]/div/div[4]/div[3]/div[2]/div[6]/div[5]/div[2]/p").text
    time.sleep(2)
    assert two_items_price == total_price


def test_Total_Price_is_correct_3_items(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "MEN").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Clothing").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "T-Shirts & Tops").click()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        "//*[@id=\"product-search-results\"]/div[2]/div[2]/div[2]/div/div[1]/div[6]/div/div/div[1]/a[1]/img").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".swatch-rect-off-white").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".size-radio:nth-child(3) .size-value").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".add-to-cart > .right_arrow_main").click()
    time.sleep(2)
    driver.get("https://www.adidas.co.il/en/cart")
    time.sleep(3)
    my_quan = Select(driver.find_element(By.XPATH, "//select[contains(@class,'quantity')]"))
    my_quan.select_by_visible_text('3')
    time.sleep(2)
    two_items_price = driver.find_element(By.XPATH,
                                          "//*[@id=\"maincontent\"]/div/div[4]/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div").text
    total_price = driver.find_element(By.XPATH,
                                      "//*[@id=\"maincontent\"]/div/div[4]/div[3]/div[2]/div[6]/div[5]/div[2]/p").text
    time.sleep(2)
    assert two_items_price == total_price
