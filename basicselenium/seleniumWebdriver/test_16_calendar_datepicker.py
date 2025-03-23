from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.firefox import GeckoDriverManager

class TestCalendarSelection(): #working 7/18/2020

    def test_datepicker(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://jqueryui.com/datepicker/")

        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

        calMonth = driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']")
        allValidDates = calMonth.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")
        time.sleep(2)

        for date in allValidDates:
            print(date.text)
            if date.text == "15":
                date.click()
                break

        driver.quit()