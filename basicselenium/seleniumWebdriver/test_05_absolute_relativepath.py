import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#=====================================================================================
# change method color-setting--eiditor--color Scheme--Pythod--function--Method call
#=====================================================================================

class TestAbsoluteVsRelativePath():

	def test_absoluteRelativePath(self):
		driver = webdriver.Chrome()
		driver.get("https://demo.automationtesting.in/Register.html")
		driver.maximize_window()

		driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/form/div[1]/div[1]/input").send_keys("David")
		driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Lee")
		time.sleep(2)
		driver.quit()