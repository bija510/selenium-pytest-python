from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
	#driver = webdriver.Chrome()
	if browser == 'chrome':
		driver = webdriver.Chrome()
		print("Lunching Chrome browser")

	elif browser == 'firefox':
		driver = webdriver.Firefox()
		print("Lunching Firefox browser")

	else:
		driver = webdriver.Ie()
	return driver


def pytest_addoption(parser): # this will get the value from CLI / hooks
	parser.addoption("--browser")

@pytest.fixture()
def browser(request): # this will return the browser value from setup method
	return request.config.getoption("--browser")

#py.test -v -s test_login.py --browser chrome
#py.test -v -s test_login.py --browser firefox