import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestMiscFunction():

	def test_misc_function(self):
		driver = webdriver.Chrome()
		driver.get("https://www.facebook.com/login/")
		driver.set_page_load_timeout(10)
		driver.delete_all_cookies()
		print("==>"+driver.current_url)
		print("==>" + driver.title)
		print("==>" + driver.current_window_handle)

		loginbtn = driver.find_element(By.XPATH, "//button[@id='loginbutton']")
		loginbtn.submit()
		time.sleep(2)
		driver.quit()
