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

	@pytest.mark.regression
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
			self.driver.close()
			self.logger.error("----------test_login page verification Passed---------")

		else:
			self.driver.save_screenshot("../Screenshot/" + "test_login1.png")
			self.driver.close()
			self.logger.error("----------test_login page verification Failed---------")
			assert False

		#self.driver.close()


