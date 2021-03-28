import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#=====================================================================================
# change method color-setting--eiditor--color Scheme--Pythod--function--Method call
#=====================================================================================

class TestAbsoluteVsRelativePath():

	def test_absoluteRelativePath(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.get("https://www.facebook.com/signup")
		driver.maximize_window()
	#absolute Path = start from root not prefered
		driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/div[1]/input").send_keys("David")
	#Relative start from middle anywhere is prefered
		driver.find_element_by_xpath("//*[@id='u_0_p']").send_keys("Lee")
		time.sleep(2)