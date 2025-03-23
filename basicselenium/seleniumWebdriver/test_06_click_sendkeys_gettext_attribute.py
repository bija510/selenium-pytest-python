from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestClickSendkeysGetTextAttribute:

	def test_basic(self):
		driver = webdriver.Chrome()
		driver.get("http://demo.automationtesting.in/Register.html")
		driver.maximize_window()
		firstName_txt = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
		firstName_txt.send_keys("David")

		movie_chk = driver.find_element(By.XPATH, "//input[@id='checkbox1']")
		movie_chk.click()

		pageLabel = driver.find_element(By.XPATH, "//h2[text()='Register']")
		print(pageLabel.text + "==> This is the page label")

		print(firstName_txt.get_attribute("value") + "==> This is the page attribute of firstName")
		time.sleep(2)

		driver.quit()
