import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#=====================================================================================
# change method color-setting--eiditor--color Scheme--Pythod--function--Method call
#=====================================================================================

class TestDropdownlist():

	def test_dropdown(self):
		driver = webdriver.Chrome()
		driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

		selectDDL = Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
		selectDDL.select_by_visible_text("Option1")
		time.sleep(2)
		selectDDL.select_by_index(2)
		time.sleep(2)
		selectDDL.select_by_value("option3")
		time.sleep(2)

		driver.quit()