from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestAutoComplete():

    def test_tooltip(self):
        driver = webdriver.Chrome(executable_path= ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://jqueryui.com/tooltip/")
        driver.implicitly_wait(3)
        driver.switch_to.frame(0)

        ageBox =driver.find_element_by_id("age")
        toolTipText =ageBox.get_attribute("title")
        print("====> "+toolTipText)
