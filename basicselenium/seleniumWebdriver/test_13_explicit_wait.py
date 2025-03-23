import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

class TestExplicitWait():

	def test_explicit_wait(self):
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

		wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
		wait.until(element_to_be_clickable((By.XPATH, "//*[@id='autocomplete']"))).send_keys("David")

		time.sleep(2)
		driver.quit()


	def test_explicit_demo(self):
		driver = webdriver.Chrome()
		driver.maximize_window()

		ewait = WebDriverWait(driver, 20)
		driver.get("http://demo.automationtesting.in/Loader.html")
		driver.find_element(By.CSS_SELECTOR,"button#loader").click()
		ewait.until(visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-default"))).click()
		time.sleep(2)
		driver.quit()
