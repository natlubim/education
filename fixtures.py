import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    page = driver.get('https://www.tiffany.com/Customer/Account/Signin.aspx')
    yield driver
    driver.close()

def login(browser):
    # находим выпадающий список с выбором языка
    elem = browser.find_element_by_name("txtEmail")
    print(input("natilubimenko@gmail.com"))
    elem = browser.find_element_by_name("txtPassword")
    print(input("N30089434l"))
    elem = browser.find_element_by_id("btnSignIn")
    elem.click()


