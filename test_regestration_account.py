import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver_binary = r".\drivers\chromedriver.exe"
    ser_chrome = ChromeService(chrome_driver_binary)
    driver = webdriver.Chrome(service=ser_chrome)
    yield driver
    driver.close()


def test_user_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.set_window_size(1012, 816)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#form > div.d-flex.justify-content-center.account-login > "
                                         "div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > "
                                         "div.gl-flex-display > button").click()
    driver.find_element(By.ID, "login-firstname").send_keys("at")
    driver.find_element(By.ID, "login-lastname").send_keys("tes")
    driver.find_element(By.CSS_SELECTOR, ".gl-radio-input__option:nth-child(1) > .gl-radio-input__label").click()
    driver.find_element(By.ID, "login-email").click()
    driver.find_element(By.ID, "login-email").send_keys("a_tessts_pytest@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#login-password").send_keys("Hh123456789+")
    time.sleep(3)
    driver.find_element(By.NAME, "age").click()
    time.sleep(3)
    driver.find_element(By.NAME, "doc-tnc-memb").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content").click()
    actualUrl = driver.current_url
    assert actualUrl == "https://www.adidas.co.il/en/account"


def test_user_signin_successfully(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.set_window_size(1012, 816)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#login-email").send_keys("haithamodeh57@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#login-password").send_keys("Hh123456789+")
    driver.find_element(By.CSS_SELECTOR, "#ok").click()
    actualUrl = driver.current_url
    assert actualUrl == "https://www.adidas.co.il/en/account"


# Negative Scenarios
def test_user_signin_email_err(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    driver.set_window_size(1012, 816)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#login-email").send_keys("haitham1odeh57@gmail.com.")
    driver.find_element(By.CSS_SELECTOR, "#ok").click()
    err_email_message = driver.find_element(By.CSS_SELECTOR,
                                            "#form > div.d-flex.justify-content-center.account-login > div:nth-child("
                                            "1) > div > div > div.gl-vspace > div > div > div").text
    assert err_email_message == "Please enter a valid e-mail address"


def test_first_name_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()

    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    err_firstname_message = driver.find_element(By.CSS_SELECTOR,
                                                "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(7) > div > div").text
    assert err_firstname_message == "Please enter a valid first name"


def test_last_name_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()

    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    err_firstname_message = driver.find_element(By.CSS_SELECTOR,
                                                "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(9) > div > div").text
    assert err_firstname_message == "Please enter a valid last name"


def test_gender_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()

    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    err_firstname_message = driver.find_element(By.CSS_SELECTOR,
                                                "#gender-hint--error").text
    assert err_firstname_message == "Please select gender"


def test_email_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()

    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    err_firstname_message = driver.find_element(By.CSS_SELECTOR,
                                                "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div.gl-vspace > div > div > div").text
    assert err_firstname_message == "Please enter a valid e-mail address"


def test_password_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()

    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    err_firstname_message = driver.find_element(By.CSS_SELECTOR,
                                                "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(16) > div > div > div > div > div.gl-form-hint.gl-form-hint--error.gl-form-hint--error--show").text
    assert err_firstname_message == "Please enter your password"


def test_confirm_age_mandatory_message_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()

    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    err_firstname_message = driver.find_element(By.CSS_SELECTOR,
                                                "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div.gl-checkbox.gl-form-item--required.gl-form-item--error > div").text
    assert err_firstname_message == "Please confirm your age"


def test_x_icon_first_name_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()

    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    time.sleep(3)
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(7) > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#cross-small"


def test_v_icon_first_name_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()
    driver.find_element(By.ID, "login-firstname").send_keys("hi")
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(7) > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#checkbox-checkmark"


def test_x_icon_second_name_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()
    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    time.sleep(3)
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(9) > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#cross-small"


def test_v_icon_second_name_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()
    driver.find_element(By.ID, "login-lastname").send_keys("hi")
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(9) > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#checkbox-checkmark"


def test_x_icon_email_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()
    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    time.sleep(3)
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div.gl-vspace > div > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#cross-small"


def test_v_icon_email_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()
    driver.find_element(By.ID, "login-email").send_keys("h@h.com")
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div.gl-vspace > div > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#checkbox-checkmark"


def test_x_icon_password_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()
    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    time.sleep(3)
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(16) > div > div > div > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#cross-small"


def test_v_icon_password_input_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()
    driver.find_element(By.ID, "login-password").send_keys("Aa123456+")
    element_after = driver.find_element(By.CSS_SELECTOR,
                                        "#form > div.d-flex.justify-content-center.account-register > div:nth-child(1) > div > div > div:nth-child(16) > div > div > div > div > svg > use")
    x_appeard = element_after.get_attribute('xlink:href')
    assert x_appeard == "#checkbox-checkmark"


def test_incorrect_input_first_name_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()

    driver.find_element(By.ID, "login-firstname").send_keys("11223344")

    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    err_firstname_message = EC.visibility_of((By.XPATH, "//*[@id=\"form\"]/div[1]/div[1]/div/div/div[5]/div/div"))
    assert bool(err_firstname_message) is True


def test_incorrect_input_last_name_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()
    time.sleep(1)

    driver.find_element(By.ID, "login-lastname").send_keys("3344")

    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    err_secondname_message = EC.visibility_of((By.XPATH, "//*[@id=\"form\"]/div[1]/div[1]/div/div/div[7]/div/div"))
    assert bool(err_secondname_message) is True


def test_incorrect_input_email_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()
    time.sleep(1)

    driver.find_element(By.ID, "login-email").send_keys("wwwww33@44.")

    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    err_email_message = EC.visibility_of((By.XPATH, "//*[@id=\"form\"]/div[1]/div[1]/div/div/div[11]/div/div/div"))
    assert bool(err_email_message) is True


message_for_password_input_incorrect = [f"test password incorrect input"]


def test_incorrect_input_password_reg(driver):
    driver.get("http://www.adidas.co.il/en")
    driver.find_element(By.CSS_SELECTOR, ".affirm").click()
    # driver.set_window_size(1170, 800)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".navbar-toggler:nth-child(1)").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#sg-navbar-collapse > nav > div.menu-group > ul > li:nth-child(8) > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#form > div.d-flex.justify-content-center.account-login > ""div.col-s-12.col-l-10.offset-l-1.gl-image > div > div.gl-hspace > ""div.gl-flex-display > button").click()
    time.sleep(1)

    driver.find_element(By.ID, "login-password").send_keys("wwwww33")

    driver.find_element(By.CSS_SELECTOR, 'html').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    driver.find_element(By.ID, "btnregistration").click()
    err_password_message = EC.visibility_of(
        (By.XPATH, "//*[@id=\"form\"]/div[1]/div[1]/div/div/div[13]/div/div/div/div/div[2]"))
    assert bool(err_password_message) is True
