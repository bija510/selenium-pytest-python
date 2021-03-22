import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Screenshot():

	def test_screenshot(self):
		driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		driver.maximize_window()
		driver.get("https://letskodeit.teachable.com/")
		driver.implicitly_wait(3)

		driver.find_element(By.LINK_TEXT, "Login").click()
		# = "C:\\Users\\Bijaya Chhetri\\workspace_python\\SeleniumWDTutorial\\zTemp\\test.png"
		destinationFileName	= "../zTemp/" + "test_Homepage1"+ str(round(time.time()*1))+".png"
		try:
			driver.save_screenshot(destinationFileName)
			print("Screenshot saved to directory --> :: " + destinationFileName)
		except NotADirectoryError:
			print("Not a directory issue")

cc = Test_Screenshot()
cc.test_screenshot()