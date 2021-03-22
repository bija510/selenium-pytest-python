from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class testClass:

	def testMethod(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.get("http://demo.automationtesting.in/Register.html")
		driver.maximize_window()
		firstName_txt = driver.find_element_by_xpath("//input[@placeholder='First Name']")
		firstName_txt.send_keys("David")

		movie_chk = driver.find_element_by_xpath("//input[@id='checkbox1']")
		movie_chk.click()

		pageLabel = driver.find_element_by_xpath("//h2[contains(text(),'Register')]")
		print(pageLabel.text + "==> This is the page label")

		print(firstName_txt.get_attribute("value") + "==> This is the page attribute of firstName")

cc = testClass()
cc.testMethod()