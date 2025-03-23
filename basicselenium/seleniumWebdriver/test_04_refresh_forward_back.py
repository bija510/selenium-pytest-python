import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#=====================================================================================
# change method color-setting--eiditor--color Scheme--Pythod--function--Method call
#=====================================================================================

class TestRefreshForwardBack():

	def test_basic(self):
		driver = webdriver.Chrome()
		driver.get("https://www.facebook.com")
		driver.maximize_window()
		driver.refresh()
		time.sleep(2)

		forgetPwdLink = driver.find_element(By.LINK_TEXT, "Forgot password?")
		forgetPwdLink.click()
		time.sleep(2)
		driver.back()
		time.sleep(2)
		driver.forward()

		driver.quit()