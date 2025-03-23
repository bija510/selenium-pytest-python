import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAlert():

    def test_alert(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
        #Example:-1
        driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        # Example:-2
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        #we need to switch so that we can come back to page and start working with other element
        driver.switch_to.default_content()

        time.sleep(2)
        driver.quit()

