import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestOpenCloseBrowser():

	def test_openClose1(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.get("https://www.facebook.com")
		time.sleep(3)
		driver.quit()

	def test_openCLose2(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.execute_script("window.location = 'https://www.amazon.com';")
		time.sleep(3)
		driver.quit()
