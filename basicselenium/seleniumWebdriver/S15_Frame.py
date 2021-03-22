import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class Test_Frame():

    def test(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.get("https://jqueryui.com/datepicker/")

        usingFrameElement = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(usingFrameElement)
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='datepicker']").click()


    def test2(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")

        usingID = "courses-iframe"
        driver.switch_to.frame(usingID)

        #driver.switch_to.frame(0) #Using Index
        driver.find_element_by_id("search-courses").send_keys("python")
        time.sleep(2)

cc = Test_Frame()
cc.test2()