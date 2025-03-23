import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

#=====================================================================================
# change method color-setting--eiditor--color Scheme--Pythod--function--Method call
#=====================================================================================

class TestCheckBoxRadBtn():

	def test_checkbx_radbtn(self):
		driver = webdriver.Chrome()
		driver.get("http://demo.automationtesting.in/Register.html")

		movieCheBx = driver.find_element(By.XPATH,"//input[@id='checkbox1']")
		# movieCheBx.click()
		# time.sleep(2)

		if (movieCheBx.is_selected())!= True:
			movieCheBx.click()

		maleRadBtn = driver.find_element(By.XPATH,"//input[@value='Male']")
		maleRadBtn.click()
		time.sleep(2)