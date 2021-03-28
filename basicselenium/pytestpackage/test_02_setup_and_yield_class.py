
# Run from cmd package level
# To run individual --> py.test -s test_02_setup_and_yield_class.py
#       to run all --------------> py.test -v -s
#       to run only one class ---> py.test -v -s test_02_setup_and_yield_class.py
#       to run only one method --> py.test -v -s test_02_setup_and_yield_class.py::test_methodA
# Pytest Fixture Update
# After pytest version 2.10, you do not need @pytest.yield_fixture explicitly to use yield.
# The default @pytest.fixture also supports yield.
# It means the code will work if you are using @pytest.yield_fixture or @pytest.fixture.
# http://doc.pytest.org/en/latest/fixture.html

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
#=================================================================================================
# This is beforeMethod & afterMethod Means==> setUp and yield will run before & after every method
#=================================================================================================
#With using class
class TestDemo2: # On using class we have to use self variable
    @pytest.yield_fixture()    # or @pytest.fixture()
    def setUp(self):
        global driver # yield driver
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("http://demo.automationtesting.in/Register.html")

        yield
        time.sleep(2)
        driver.quit()

    def test_methodA(self, setUp):
        driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Ram")

    def test_methodB(self, setUp):
        driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Sharma")
