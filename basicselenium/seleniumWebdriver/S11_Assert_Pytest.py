from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Testclass():

	def test_demo(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.get("https://www.facebook.com")

		assert "ball" == "bll"

		assert "dog" != "cat"

		if driver.title=="Facebook - Log In or Sign Up":
			assert True  # assert True

# py.test -v -s TestCases/S11_Assert_Pytest.py