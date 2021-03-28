import os
import time
import autoit
from selenium import webdriver
########################################################################
# Just need to CMD  pip install [ PyAutoIt = 0.6.0] That all Nothing else
# https://stackoverflow.com/questions/8665072/how-to-upload-file-picture-with-selenium-python
########################################################################
class TestPyAutoIt:

	def test_PyAutoItFileUpload(self):
		driver = webdriver.Chrome()
		driver.get("http://demo.automationtesting.in/FileUpload.html")
		driver.maximize_window()

		#path = rawpath.replace("\\", "/") this need on send_keys but not here

		uploadBtn = driver.find_element_by_xpath("//div[@class='btn btn-primary btn-file']")
		uploadBtn.click()

		path = (os.getcwd() + "\\uploadFile.txt")
		autoit.win_wait_active("Open")
		autoit.control_set_text("Open", "Edit1", path)
		autoit.send("{ENTER}")
		time.sleep(5)
