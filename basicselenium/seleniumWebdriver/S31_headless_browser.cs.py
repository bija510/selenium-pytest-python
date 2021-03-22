from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

class TestHeadless:

	def test_chrome(self):
		options = webdriver.ChromeOptions()
		options.headless =True
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
		driver.implicitly_wait(5)

		driver.get("https://www.amazon.com")
		print(driver.title +"========headless execution in Chrome=========")

	def test_firefox(self):
		options = webdriver.FirefoxOptions()
		options.headless = True
		driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
		driver.implicitly_wait(5)
		driver.get("https://www.facebook.com")
		print(driver.title +"========headless execution in Firefox=========")

# pytest -v -s test_headless.py::TestHeadless::test_chrome
# pytest -v -s test_headless.py::TestHeadless::test_firefox
# in Terminal just write command ... Once then Just click UP_ARROW or DOWN_ARROW ==> will give previous command