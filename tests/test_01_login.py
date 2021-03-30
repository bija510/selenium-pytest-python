from pages.loginPage import LoginPage
import pytest
from utilites.custom_logger import logGen
from utilites.read_ini_file import ReadConfig
import time

#@pytest.mark.usefixtures('setup') we can do this insted of writing setup in everymethod
class TestloginClass(): #Class name should start from >>--> Test and method name test_methodname
	baseUrl = ReadConfig.getApplicationURL()
	userName = ReadConfig.getUserName()
	password = ReadConfig.getPassword()

	logger = logGen.loggen()

	@pytest.mark.regression
	def test_homePageTitle(self, setup):
		self.logger.info("----------TestloginClass---------")
		self.logger.info("----------Verifying HomePage Title---------")
		self.driver = setup
		self.driver.get(self.baseUrl)
		actTitle = self.driver.title

		if actTitle =='OrangeHRM':
			assert True
			self.logger.info("----------Home page verification Passed---------")
		else:
			self.driver.save_screenshot("../screenshots/" + "test_Homepage1"+ str(round(time.time()*1))+".png")
			self.logger.error("----------Home page verification Failed---------")
			assert False

	@pytest.mark.smoke
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
			self.logger.error("----------test_login page verification Passed---------")

		else:
			self.driver.save_screenshot("../screenshots/" + "test_login"+ str(round(time.time()*1))+".png")
			self.logger.error("----------test_login page verification Failed---------")
			assert False


		#NOTE:- To run Cmd & local both works
		# C:\Users\Bijaya Chhetri\workspace_python\selenium-pytest-python>pytest -v -s tests\test_01_login.py

