from selenium import webdriver
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest

# @pytest.fixture() ==>This is ByDefault for the method (setup) @BeforeTest & @AfterTest
# @pytest.fixture(scope= 'class') ==>This will for for class level (oneTimeSetUp) @BeforeClass & @AfterClass
# @pytest.fixture(scope= 'module') not much used
# @pytest.yield_fixture() ==@pytest.fixture() now this is considered same
# if there is yield === NO return can be used

@pytest.yield_fixture()
def setup():
    browser = "edge"
    if browser == 'ie':
        driver = webdriver.Ie(executable_path=IEDriverManager().install())  # No maxmize need
        driver.implicitly_wait(10)
        print("Lunching IE browser")

    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) #No maxmize need
        driver.implicitly_wait(10)
        print("Lunching Firefox browser")

    elif browser == 'edge':
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        print("Lunching Edge browser")

    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        print("Lunching Chrome browser")

    yield driver #This is equal to return driver
    print("---This return driver and closing it---")
    driver.quit()

#NOTE: we have issue conficting --browser argument NOT WORKING
# def pytest_addoption(parser): # this will get the value from CLI / hooks
#     parser.addoption("--browser")

# @pytest.fixture()
# def browser(request): # this will return the browser value from setup method
#     return request.config.getoption("--browser")
#
# ########### pytest HTML Report ################
#
# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'letskodeit'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Bijay'
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

#py.test -v -s test_01_login.py --browser chrome
#py.test -v -s test_01_login.py --browser firefox
#py.test -v -s --html=../Reports/report.html test_01_login.py --browser chrome


