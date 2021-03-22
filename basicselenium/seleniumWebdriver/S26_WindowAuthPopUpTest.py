import time
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Test_WindowAithentacatin():

    def test(self):
        driver = webdriver.Edge(executable_path= EdgeChromiumDriverManager().install())
        driver.maximize_window()

        # driver.get("http://the-internet.herokuapp.com/")

        #############this is the window authentication popUp##############
        userName ="admin"
        password = "admin@"
        driver.get("http://"+userName+ ":" +password+ "the-internet.herokuapp.com/")
        time.sleep(2)
        driver.find_element_by_link_text("Basic Auth").click()
        time.sleep(2)

cc = Test_WindowAithentacatin()
cc.test()