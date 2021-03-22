import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class AutoComplete():

    def test(self):
        driver = webdriver.Chrome(executable_path= ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.google.com/")
        driver.implicitly_wait(3)

        cityField = driver.find_element(By.XPATH,"//input[@name='q']")
        cityField.send_keys("python")

        cityField.send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, "//div[@class='a4bIc']//input[@name='q']").click()
        driver.find_element(By.XPATH, "//div[@class='a4bIc']//input[@name='q']").send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='a4bIc']//input[@name='q']").send_keys(Keys.ARROW_DOWN)
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='a4bIc']//input[@name='q']").send_keys(Keys.ENTER)

        # driver.quit()

ff = AutoComplete()
ff.test()