import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#py.test -v -s TestCases/S22_DisplayedSelectedEnabled.py::test_selAndDescleted
###############################################################################################
@pytest.fixture()
def setUp():
	global driver  # yield driver
	driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
	driver.maximize_window()

	yield
	time.sleep(2)
	driver.quit()
###############################################################################################

def test_selAndDescleted(setUp):
	driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
	# Example:-1
	option1TxtBx = driver.find_element_by_xpath("//input[@id='checkBoxOption1']")
	assert option1TxtBx.is_selected() == False

	# Example: - 2
	showHideTxtBx = driver.find_element_by_xpath("//input[@id='displayed-text']")
	assert showHideTxtBx.is_displayed() == True

###############################################################################################
def test_isEnabled(setUp):
	driver.get("http://www.testdiary.com/training/selenium/selenium-test-page/")
	saveBtn = driver.find_element_by_xpath("//button[@id='demo']")
	print("is Btn Enabled?:- " + saveBtn.is_enabled())
