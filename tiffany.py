import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TiffanyCom (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()


    def test_login_logout(self):
        driver = self.driver
        driver.get("https://www.tiffany.com/Customer/Account/Signin.aspx")
        time.sleep(5)

        elem = driver.find_element_by_name("txtEmail")
        elem.send_keys("natilubimenko@gmail.com")
        time.sleep(5)
        elem = driver.find_element_by_name("txtPassword")
        elem.send_keys("N30089434l")
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)

        driver.get("https://www.tiffany.com/Customer/Account/sign_out_success.aspx")
        time.sleep(10)



    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
