import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common import keys

class Test_webTable():

    def test_tableRow(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.w3schools.com/html/html_tables.asp")

        firstRowElement = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[2]/td")
        for ele in firstRowElement:
            print(ele.text)


    def clickOrGetText_From_Any_tableTD_test(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.w3schools.com/html/html_tables.asp")
        driver.execute_script("window.scrollBy(0,300)")
        tableDatas = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr/td")
        for i in range(len(tableDatas)):
            #print(i, tableDatas[i].text) # will print all the TD text from Table
            if tableDatas[i].text == "Island Trading":
                print(tableDatas[i+1].text)

cc= Test_webTable()
cc.clickOrGetText_From_Any_tableTD_test()


#===========Pytest Start from here===============
# pytest -v -s TestCases/S17_WebTable_HtmlTable.py