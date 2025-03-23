import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestMouseHovering():

    def test_KeysCommand(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://demo.automationtesting.in/Register.html")
        driver.implicitly_wait(3)

        firstNameTxt =driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[1]/div[1]/input")
        firstNameTxt.send_keys(Keys.SHIFT, "ram")

        webTableTab = driver.find_element(By.XPATH,"//a[contains(text(),'WebTable')]")

        webTableTab.send_keys(Keys.CONTROL, Keys.ENTER)
        time.sleep(3)
