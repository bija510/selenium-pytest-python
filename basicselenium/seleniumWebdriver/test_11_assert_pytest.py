from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestAssertPytest():

	def test_assert_pytest(self):
		driver = webdriver.Chrome()
		driver.get("https://www.facebook.com")

		assert "ball" == "ball"

		assert "dog" != "cat"

		if driver.title=="Facebook - Log In or Sign Up":
			assert True  # assert True

# py.test -v -s TestCases/test_11_assert_pytest.py