from pagesObjects.loginPage import LoginPage
from selenium import webdriver
import pytest
from utilites.customLogger import logGen
from utilites.readProperties import ReadConfig

class TestloginClass():
	baseUrl = ReadConfig.getApplicationURL()
	userName = ReadConfig.getUserName()
	password = ReadConfig.getPassword()

	logger = logGen.loggen()

	def test_homePageTitle(self, setup):
		self.logger.info("----------TestloginClass---------")
		self.logger.info("----------Verifying HomePage Title---------")
		self.driver = setup
		self.driver.get(self.baseUrl)
		actTitle = self.driver.title

		if actTitle =='OrangeHRM':
			assert True
			self.driver.close()
			self.logger.info("----------Home page verification Passed---------")
		else:
			self.driver.save_screenshot(
				"../Screenshot/" + "testHomepage1.png")
			self.driver.close()
			self.logger.error("----------Home page verification Failed---------")
			assert False


	def test_login(self, setup):
		self.driver = setup
		self.driver.get(self.baseUrl)

		self.lp = LoginPage(self.driver)
		self.lp.setUserName(self.userName)
		self.lp.setPassword(self.password)
		self.lp.clickLoginButton()
		actTitle = self.driver.title

		if actTitle == 'OrangeHRM':
			assert True
			self.driver.close()
			self.logger.error("----------test_login page verification Passed---------")

		else:
			self.driver.save_screenshot("../Screenshot/" + "test_login1.png")
			self.driver.close()
			self.logger.error("----------test_login page verification Failed---------")
			assert False

		#self.driver.close()

"""
#py.test -v -s test_login.py
#py.test -v -s test_login.py --browser chrome
#py.test -v -s test_login.py --browser firefox
#Run parallel max -3 ===>How many method we have just pass num
#py.test -v -s -n=2 test_login.py --browser chrome
# To run Anything we have to Run from CMD or terminal ==r-click package -->
# Open in terminal --> py.test
# To run full with details--> py.test -v -s
# To run individual --> py.test -s test_case_demo1.py
"""

