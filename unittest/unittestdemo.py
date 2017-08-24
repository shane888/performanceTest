#usr/bin/python
#encoding:utf-8
import time
from appium import webdriver
import unittest
from ddt import ddt, data, unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.mook.mook'
        desired_caps['appActivity'] = '.LoginActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @data(("mooktest@sogou.com", "mooktest", False),
          ("mooktest", "mooktest", True),
          ("#$@%^", "735522@@", True))
    @unpack
    def testLogIn(self, username, password, expectedresult):
        self.driver.find_element_by_id("email").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("email_sign_in_button").click()

        try:
            if self.driver.find_element_by_id("email_sign_in_button").is_displayed():
                exist = True
        except Exception, e:
            exist = False
        self.assertEqual(exist, expectedresult)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
