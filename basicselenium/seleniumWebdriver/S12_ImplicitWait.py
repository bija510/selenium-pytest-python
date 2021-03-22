import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class refreshForBack():

	def test1(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.get("https://www.facebook.com")
		driver.implicitly_wait(10)
		forgetPwdLink = driver.find_element_by_xpath("//a[normalize-space()='Forgot Password?']")
		forgetPwdLink.click()
		time.sleep(2)


cc = refreshForBack()
cc.test1()