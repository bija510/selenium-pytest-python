from selenium import webdriver
import time
import os

class TestFileUpload():

    def test_upload_using_sendkeys(self):
        global driver
        try:
            #Only work if there is [type= "file"] attribute Other wise ask developer to add that
            #or to find demo site convert word to pdf file and use that website

            driver = webdriver.Chrome()
            driver.get("http://demo.automationtesting.in/FileUpload.html")
            driver.maximize_window()

            rawpath = (os.getcwd() + "\\uploadFile.txt")
            path = rawpath.replace("\\", "/")

            driver.find_element_by_css_selector("input[name='input4[]']").send_keys(path)
            time.sleep(3)

        #except Exception as e:
            #print(str(e))

        finally:
            driver.close()

