from fixtures import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located



def test_login (browser):
    elem = browser.find_element_by_id("txtEmail")
    # вводим заголовок страницы
    elem.send_keys("natilubimenko@gmail.com")
    elem = browser.find_element_by_id("txtPassword")
    # вводим заголовок страницы
    elem.send_keys("N30089434l")
    # находим и жмем кнопку "Проверить"
    elem = browser.find_element_by_id("btnSignIn")
    elem.click()

    wait = WebDriverWait(browser, 20)
