"""
file name should start with test
test method name should start with test
py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test test_module.py::test_method  # only run test_method in test_module
-s to print statements
-v verbose
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

#=======================================================================================================
# This is BeforeTest & AfterTest Means==> setUp and teardown will only 1 time before & after all methods
#=======================================================================================================
driver = None
def setup_module(module):#only run once
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")


def teardown_module(module): #only run once
    driver.quit()


def test_google_title():
    assert driver.title == "Google"


def test_google_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"