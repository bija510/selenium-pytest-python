import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#=====================================================================================
# change method color-setting--eiditor--color Scheme--Pythod--function--Method call
#=====================================================================================

class refreshForBack():

	def test1(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.get("https://www.facebook.com")
		driver.refresh()
		time.sleep(2)
		forgetPwdLink = driver.find_element_by_xpath("//a[normalize-space()='Forgot Password?']")
		forgetPwdLink.click()
		time.sleep(2)
		driver.back()
		time.sleep(2)
		driver.forward()

cc = refreshForBack()
cc.test1()