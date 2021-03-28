import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class TestAlert():

    def test_alert(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
        #Example:-1
        driver.find_element_by_xpath("//input[@id='alertbtn']").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        # Example:-2
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='alertbtn']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        #we need to switch so that we can come back to page and start working with other element
        driver.switch_to.default_content()

