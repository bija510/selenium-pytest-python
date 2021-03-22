import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

#=====================================================================================
# change method color-setting--eiditor--color Scheme--Pythod--function--Method call
#=====================================================================================

class Dropdownlist():

	def test1(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

		selectDDL = Select(driver.find_element_by_xpath("//select[@id='dropdown-class-example']"))
		selectDDL.select_by_visible_text("Option1")
		time.sleep(2)
		selectDDL.select_by_index(2)
		time.sleep(2)
		selectDDL.select_by_value("option3")
		time.sleep(2)


cc = Dropdownlist()
cc.test1()