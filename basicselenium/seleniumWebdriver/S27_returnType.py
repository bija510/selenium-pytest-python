import time
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#####################################################################################
def name():
    firstName = "David"
    return firstName
#####################################################################################
def driverReturn():
    driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    return driver
#####################################################################################
class Test_Returntype():

    def test(self):
        driver = driverReturn()
        driver.maximize_window()
        driver.get("http://demo.automationtesting.in/Register.html")

        driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys(name())
        time.sleep(2)
#####################################################################################


cc = Test_Returntype()
cc.test()