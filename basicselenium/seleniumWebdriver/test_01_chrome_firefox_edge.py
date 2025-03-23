from selenium import webdriver
import time
#==================================================================
# pytest documentation Naming conventions Strickly need to follow
# file name = should start or end with “test” ===> test_example.py
# class name should start with “Test”,===========> TestExample
# method name should start with "test_"==========> test_example
#==================================================================
class TestLocalDriver():

    def test_Chrome(self):
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")
        driver.maximize_window()
        print(driver.capabilities.get('browserName'))
        time.sleep(3)
        driver.quit()

    def test_Firefox(self):
        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")
        driver.maximize_window()
        print(driver.capabilities.get('browserName'))
        time.sleep(3)
        driver.quit()

    def test_Edge(self):
        driver = webdriver.Edge()
        driver.get("http://www.letskodeit.com")
        driver.maximize_window()
        print(driver.capabilities.get('browserName'))
        time.sleep(3)
        driver.quit()

