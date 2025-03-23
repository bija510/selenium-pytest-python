import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAutoComplete():

    def test_dynamic_dropdown(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.implicitly_wait(3)

        cityField = driver.find_element(By.XPATH,"//input[@id='autocomplete']")
        cityField.send_keys("Nep")

        cityField.send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, "//input[@id='autocomplete']").click()
        driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys(Keys.ENTER)

        time.sleep(2)
        driver.quit()
