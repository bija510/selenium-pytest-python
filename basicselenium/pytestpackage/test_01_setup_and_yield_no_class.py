# To Install cmd-->pip3 install pytest or file/setting/project.projectInterpeter/ then + & install
# To run Anything we have to Run from CMD or terminal
# Open in terminal --> py.test
# To run full with details--> py.test -v -s
# To run file or class --> py.test -s test_01_setup_and_yield_no_class.py
#To run single method -->pytest -v -s test_01_setup_and_yield_no_class.py::test_methodB
# Pytest Naming Conventions
# If we don't follow naming conventions, then pytest will not pick up tests from the file.
# File names should start or end with ===> “test”, example_test.py
# Class name should start with or End with===> “Test”, Eg:- class TestDemo1:
# Test method names should start with “test_”, as in test_example
# official documentation :http://pytest.readthedocs.io/en/reorganize-docs/new-docs/user/naming_conventions.html

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
#=================================================================================================
# This is beforeMethod & afterMethod Means==> setUp and yield will run before & after every method
#=================================================================================================
# Without using Class
@pytest.fixture()
def setUp():
    global driver # yield driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("http://demo.automationtesting.in/Register.html")

    yield
    time.sleep(2)
    driver.quit()

def test_enterFirstName(setUp): # we write setUp here so it will run before this method
    driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Ram")

def test_enterLastName(setUp):
    driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("Sharma")

#pytest -v -s test_01_setup_and_yield_no_class.py