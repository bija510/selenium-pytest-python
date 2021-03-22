from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Test_JavascriptFunction():

    def test(self):
        driver = webdriver.Edge(executable_path= EdgeChromiumDriverManager().install())
        driver.maximize_window()
        driver.execute_script("window.location = 'http://demo.automationtesting.in/Register.html';")

        ##############Scroll Element Into View###############
        driver.execute_script("window.scrollBy(0, 1000);")  # Scroll Down
        driver.execute_script("window.scrollBy(0, -1000);") # Scroll Up

        element1 = driver.find_element_by_xpath("//button[normalize-space()='Submit']")
        driver.execute_script("arguments[0].scrollIntoView(true);", element1)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 1000);")

        location = element1.location_once_scrolled_into_view
        driver.execute_script("window.scrollBy(0, -150);")
        ############### Click ################################
        movieChx =driver.find_element_by_xpath("//input[@id='checkbox1']")
        driver.execute_script("arguments[0].click();", movieChx)

        ############### sendkeys #############################
        pnoneNumber ="1112223333"
        phoneTxt = driver.find_element_by_xpath("//input[@type='tel']")
        driver.execute_script("arguments[0].value='"+pnoneNumber+"';" ,phoneTxt)

        element = driver.execute_script("return document.querySelector(\"input[placeholder='First Name']\");")
        element.send_keys("Test")
        ############### getText ##############################
        RegisterLbl = driver.find_element_by_xpath("//h1[contains(text(),'Automation Demo Site')]")
        print(driver.execute_script("return (arguments[0].innerHTML).toString();", RegisterLbl))

        time.sleep(4)
ff = Test_JavascriptFunction()
ff.test()