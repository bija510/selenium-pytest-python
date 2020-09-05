from pagesObjects.loginPage import LoginPage
from selenium import webdriver
import pytest
from utilites.customLogger import logGen
from utilites.readProperties import ReadConfig
from utilites import XLUtils
import  time


class TestloginClass():

	##############################
	# Reading Data from Excel File
	###############################

	path = "../testData/InputData.xlsx"
	baseUrl = XLUtils.readData(path, "Sheet1", 2, 1)
	userName = XLUtils.readData(path, "Sheet1", 3, 1)
	password = XLUtils.readData(path, "Sheet1", 4, 1)

	logger = logGen.loggen()

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
			self.driver.close()
			self.logger.error("----------test_login page verification Passed---------")

		else:
			self.driver.save_screenshot("../Screenshot/" + "test_login1.png")
			self.driver.close()
			self.logger.error("----------test_login page verification Failed---------")
			assert False

	###############################
	# Writing data to Excel file
	#################################

	XLUtils.writeData(path, "Sheet1", 3, 2, "Test_LoginDDT Pass")

	# py.test -v -s test_loginDDT.py --browser chrome
	#self.driver.close()

"""
https://github.com/pavanoltraining/nopCommerceProject
# py.test -v -s test_login.py
# py.test -v -s test_login.py --browser chrome
# py.test -v -s test_login.py --browser firefox
# Run parallel max -3 ===>How many method we have just pass num
# py.test -v -s test_loginDDT.py --browser chrome
# To run Anything we have to Run from CMD or terminal ==r-click package -->
# Open in terminal --> py.test
# To run full with details--> py.test -v -s
# To run individual --> py.test -s test_case_demo1.py
# py.test -v -s --html=../Reports/report.html test_login.py --browser chrome

"""

