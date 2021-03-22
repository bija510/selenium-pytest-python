import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

#=====================================================================================
# change method color-setting--eiditor--color Scheme--Pythod--function--Method call
#=====================================================================================

class TestClass():

	def test1(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.get("http://demo.automationtesting.in/Register.html")

		movieCheBx = driver.find_element_by_xpath("//input[@id='checkbox1']")
		# movieCheBx.click()
		# time.sleep(2)

		if (movieCheBx.is_selected())!= True:
			movieCheBx.click()

		maleRadBtn = driver.find_element_by_xpath("//input[@value='Male']")
		maleRadBtn.click()
		time.sleep(2)


cc = TestClass()
cc.test1()