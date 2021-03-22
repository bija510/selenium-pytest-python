import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from wait_type.explicit_wait_type import ExplicitWaitType

class refreshForBack():

	def test1(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.maximize_window()
		driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

		wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
		wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='autocomplete']"))).send_keys("David")

		time.sleep(2)
		driver.quit()


	def test2(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.maximize_window()

		wait = ExplicitWaitType(driver)
		driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
		wait.waitForElement("userName").send_keys("Biju123")

		time.sleep(2)
		driver.quit()


cc= refreshForBack()
#cc.test1()
cc.test2()