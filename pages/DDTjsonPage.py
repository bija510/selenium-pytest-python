from selenium import webdriver
import pytest
class DDTjsonPage():

	txtFirstName_xpath = "//input[@placeholder='First Name']"
	txtLastName_xpath = "//input[@placeholder='Last Name']"
	txtAddress_xpath = "//*[@id='basicBootstrapForm']/div[2]/div/textarea"
	txtPhoneNumber_xpath = "//*[@id='basicBootstrapForm']/div[4]/div/input"

	#driver = webdriver.Chrome()
	def __init__(self, driver):
		self.driver = driver

	def openUrl(self, url):
		self.driver.get(url)

	def enterFirstName(self, firstName):
		self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstName)

	def enterLastName(self, lastName):
		self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastName)

	def enterAddress(self, address):
		self.driver.find_element_by_xpath(self.txtAddress_xpath).send_keys(address)

	def enterPhoneNumbers(self, phonenumber):
		self.driver.find_element_by_xpath(self.txtPhoneNumber_xpath).send_keys(phonenumber)
