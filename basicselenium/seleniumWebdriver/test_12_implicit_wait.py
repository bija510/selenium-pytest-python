import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestImplicitWait():

	def test_implicit_wait(self):
		driver = webdriver.Chrome()
		driver.get("https://www.facebook.com")
		driver.implicitly_wait(10)
		forgetPwdLink = driver.find_element(By.XPATH, "//a[normalize-space()='Forgot Password?']")
		forgetPwdLink.click()
		time.sleep(2)