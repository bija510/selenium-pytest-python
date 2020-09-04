from pagesObjects.loginPage import LoginPage
from selenium import webdriver
import pytest

class TestloginClass():
	baseUrl = "https://opensource-demo.orangehrmlive.com/"
	userName ="Admin"
	password = "admin123"

	def test_homePageTitle(self, setup):
		self.driver = setup
		self.driver.get(self.baseUrl)
		actTitle = self.driver.title

		if actTitle =='OrangeHR':
			assert True
		else:
			self.driver.save_screenshot(
				"../Screenshot/" + "testHomepage1.png")
			self.driver.close()
			assert False


	def test_login(self, setup):
		self.driver = setup
		self.driver.get(self.baseUrl)

		self.lp = LoginPage(self.driver)
		self.lp.setUserName(self.userName)
		self.lp.setPassword(self.password)
		self.lp.clickLoginButton()
		actTitle = self.driver.title

		if actTitle == 'OrangeHR':
			assert True
		else:
			self.driver.save_screenshot("../Screenshot/" + "test_login1.png")
			self.driver.close()
			assert False

		#self.driver.close()

#py.test -v -s test_login.py
# To run Anything we have to Run from CMD or terminal ==r-click package -->
# Open in terminal --> py.test
# To run full with details--> py.test -v -s
# To run individual --> py.test -s test_case_demo1.py

