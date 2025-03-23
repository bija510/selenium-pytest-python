import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestFrame():

    def test_using_frame_element(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://jqueryui.com/datepicker/")

        usingFrameElement = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
        driver.switch_to.frame(usingFrameElement)
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
        time.sleep(2)
        driver.quit()


    def test_using_id(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.letskodeit.com/practice")

        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)
        usingID = driver.find_element(By.ID, "courses-iframe")
        driver.switch_to.frame(usingID)


        #driver.switch_to.frame(0) #Using Index
        driver.find_element(By.XPATH,"//input[@id='search']").send_keys("python")
        time.sleep(2)
        driver.quit()

