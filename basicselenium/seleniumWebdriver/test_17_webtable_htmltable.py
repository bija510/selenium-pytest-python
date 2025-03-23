import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

class TestWebTable():

    def test_tableRow(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.w3schools.com/html/html_tables.asp")

        firstRowElement = driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr[2]/td")
        for ele in firstRowElement:
            print(ele.text)
        time.sleep(2000)
        driver.quit()


    def test_clickOrGetText_From_tableTD(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.w3schools.com/html/html_tables.asp")
        driver.execute_script("window.scrollBy(0,300)")
        tableDatas = driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr/td")
        for i in range(len(tableDatas)):
            #print(i, tableDatas[i].text) # will print all the TD text from Table
            if tableDatas[i].text == "Island Trading":
                print(tableDatas[i+1].text)

        time.sleep(2000)
        driver.quit()
