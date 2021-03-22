import pytest


# ==============================================
# @pytest.fixture(scope='class')
# @pytest.fixture(scope='method') by default
# @pytest.fixture(scope='module')
# ==============================================

@pytest.yield_fixture()
def setUp():
	print('\n=====> Before method level SETUP')
	yield
	print('\n=====> After method level TEARDOWN')


@pytest.yield_fixture(scope="module")
def oneTimeSetUp(browser, osType):
	print("Running one time setUp")
	if browser == 'firefox':
		print("Running tests on FF")
	else:
		print("Running tests on chrome")
	yield
	print("Running one time tearDown")


def pytest_addoption(parser):
	parser.addoption("--browser")
	parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
	return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
	return request.config.getoption("--osType")


# ===========================================================================
# This is new added 02/01/2021
# ===========================================================================
@pytest.fixture()
def data():
	return ('python-user', 'pypassword', 'python@demo.com')  # tuple


# this is creating a dictonary & run 3 times
@pytest.fixture(params=[
	{'user': 'user1', 'pass': 'pwd1'},
	{'user': 'user2', 'pass': 'pwd2'},
	{'user': 'user3', 'pass': 'pwd3'}
])
def data_provider(request):
	return request.param


@pytest.fixture(scope='class')
def class_fixture():
	print('\n=====>Before class Set Up')
	yield
	print('\n=====>After class Set up')

# ===========================================================================
