import os
import time
import pyautogui
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
###################################################################################################
# Just Need to [ pip install PyAutoGUI = 0.9.50 ] add ("C" driver name infront of path) For Chrome & Edge
# For Firefox no need to add "C" infront
# That all nothing else
# https://stackoverflow.com/questions/8665072/how-to-upload-file-picture-with-selenium-python
##################################################################################################
class TestPyAutoGui:
	def test_fileUploadPyAutoGui(self):

		#driver = webdriver.Edge(executable_path= EdgeChromiumDriverManager().install())
		driver = webdriver.Firefox() #Chrome()
		driver.get("http://demo.automationtesting.in/FileUpload.html")
		driver.maximize_window()

		path = (os.getcwd() + "\\uploadFile.txt")
		#path = rawpath.replace("\\", "/") this need on send_keys but not here

		uploadBtn = driver.find_element_by_xpath("//div[@class='btn btn-primary btn-file']")
		uploadBtn.click()

		#pyautogui.write("C" + path, interval=0.10 ) #original interval=0.25 For Chrome
		pyautogui.write(path, interval=0.10)  # For Firefox
		pyautogui.press('return')

		time.sleep(4)
		driver.close()


browser = TestPyAutoGui()
browser.test_fileUploadPyAutoGui()