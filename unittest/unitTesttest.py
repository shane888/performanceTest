#usr/bin/python
#encoding:utf-8
import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = '8627d0e6'
desired_caps['appPackage'] = 'com.weima.run.dev'
desired_caps['appActivity'] = '.SplashScreenActivity'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#driver.find_element_by_id("email").send_keys("mooktest")
#driver.find_element_by_id("password").send_keys("mooktest")
driver.find_element_by_id("layout_main_sum").click()

try:
    if driver.find_element_by_id("layout_main_sum").is_displayed():
        print "fail"
except Exception, e:
        print e
        print "pass"

driver.quit()

time.sleep(5)