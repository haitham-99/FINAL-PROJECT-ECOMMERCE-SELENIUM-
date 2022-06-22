import time
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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
    driver.find_element(By.ID, "login-email").send_keys("a_tests_pytest@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#login-password").send_keys("Hh123456789+")
    time.sleep(3)
    driver.find_element(By.NAME, "age").click()
    time.sleep(3)
    driver.find_element(By.NAME, "doc-tnc-memb").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#btnregistration > .gl-cta__content").click()
    actualUrl = driver.current_url
    assert actualUrl == "https://www.adidas.co.il/en/account"


def test_user_signin(driver):
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

