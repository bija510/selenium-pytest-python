from selenium import webdriver
import time

class TestLocalDriver():

    def Chrome(self):
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")
        driver.maximize_window()
        print(driver.capabilities.get('browserName'))

    def Firefox(self):
        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")
        driver.maximize_window()
        print(driver.capabilities.get('browserName'))

    def Ie(self):
        driver = webdriver.Ie()
        driver.get("http://www.letskodeit.com")
        driver.maximize_window()
        print(driver.capabilities.get('browserName'))

    def Edge(self):
        driver = webdriver.Edge(executable_path="C:/python38/Drivers/msedgedriver.exe")
        driver.get("http://www.letskodeit.com")
        driver.maximize_window()
        print(driver.capabilities.get('browserName'))

    time.sleep(5)


browser = TestLocalDriver()
browser.Firefox()
#browser.Chrome()
#browser.Ie()
#cc.Firefox()
