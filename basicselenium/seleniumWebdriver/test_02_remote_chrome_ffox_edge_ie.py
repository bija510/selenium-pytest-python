from selenium import webdriver
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class TestRemoteDriver:
    driver =None
    def test_Chrome(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.walmart.com")
        print(driver.capabilities.get('browserName'))

    def test_Ie(self):
        driver = webdriver.Ie(executable_path=IEDriverManager().install())  # No maxmize need
        driver.implicitly_wait(10)
        driver.get("https://www.walmart.com")
        print(driver.capabilities.get('browserName'))

    def test_Firefox(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) #No maxmize need
        driver.implicitly_wait(10)
        driver.get("https://www.walmart.com")
        print(driver.capabilities.get('browserName'))

    def test_Edge(self):
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.walmart.com")
        print(driver.capabilities.get('browserName'))

browser = Test_RemoteDriver()
#browser.test_Edge()
browser.test_Chrome()
#browser.test_Ie()
#cc.test_Firefox()
