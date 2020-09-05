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

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'letskodeit'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Bijay'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


#py.test -v -s test_login.py --browser chrome
#py.test -v -s test_login.py --browser firefox
#py.test -v -s --html=../Reports/report.html test_login.py --browser chrome


