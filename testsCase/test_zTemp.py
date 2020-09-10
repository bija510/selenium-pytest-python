from selenium import webdriver
from pagesObjects.DDTjsonPage import DDTjsonPage
import pytest
from utilites.customLogger import logGen

class Testdemoauto:  #Class name should start from >>--> Test
	logger = logGen().loggen()


	def test_register(self, setup):
		self.driver = setup
		self.dd = DDTjsonPage(self.driver)
		self.logger.info("----Demo automation page open---")
		self.dd.openUrl("http://demo.automationtesting.in/Register.html")
		self.dd.enterFirstName('Ram')
		self.dd.enterLastName('Sharma')
		self.dd.enterPhoneNumbers('123456789')
		self.dd.enterAddress('abc@gmail.com')


		#pytest -v -s test_zTemp.py --browser chrome