from pages.loginPage import LoginPage
from selenium import webdriver
import pytest
from utilites.custom_logger import logGen
from utilites.read_ini_file import ReadConfig
from utilites import excel_util
import time

class TestloginClass():

	##############################
	# Reading Data from Excel File
	###############################

	path = "../data/InputData.xlsx"
	baseUrl = excel_util.readData(path, "Sheet1", 2, 1)
	userName = excel_util.readData(path, "Sheet1", 3, 1)
	password = excel_util.readData(path, "Sheet1", 4, 1)

	logger = logGen.loggen()

	@pytest.mark.smoke
	def test_login(self, setup):
		self.driver = setup
		self.driver.get(self.baseUrl)

		self.lp = LoginPage(self.driver)
		self.lp.setUserName(self.userName)
		self.lp.setPassword(self.password)
		self.lp.clickLoginButton()
		actTitle = self.driver.title
		time.sleep(3)
		if actTitle == 'OrangeHRM':
			assert True
			self.logger.error("----------test_login page verification Passed---------")

		else:
			self.driver.save_screenshot("../screenshots/" + "testLoginDDT"+ str(round(time.time()*1))+".png")
			self.logger.error("----------test_login page verification Failed---------")
			assert False

	###############################
	# Writing data to Excel file
	#################################

	excel_util.writeData(path, "Sheet1", 3, 2, "Test_LoginDDT Pass")

	# py.test -v -s test_02_login_data_driven_using_excel_file.py --browser chrome
