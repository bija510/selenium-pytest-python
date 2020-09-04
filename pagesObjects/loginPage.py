from selenium import webdriver

class LoginPage():

	userNameTextBox_xpath = "//input[@id='txtUsername']"
	passwordtextBox_xpath = "//input[@id='txtPassword']"
	loginButton_xpath = "//input[@id='btnLogin']"

	#driver = webdriver.Chrome()

	def __init__(self, driver):
		self.driver = driver

	def setUserName(self, userName):
		self.driver.find_element_by_xpath(self.userNameTextBox_xpath).send_keys(userName)

	def setPassword(self, password):
		self.driver.find_element_by_xpath(self.passwordtextBox_xpath).send_keys(password)

	def clickLoginButton(self):
		self.driver.find_element_by_xpath(self.loginButton_xpath).click()

	def title(self):
		self.driver.title()


