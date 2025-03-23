from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#https://pypi.org/project/webdriver-manager/
#pip3 install webdriver_manager ----> pip3 list ---> show all the plugin list

class TestRemoteDriver:
    def test_headless_chrome(self):
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.facebook.com")
        print("===>" + driver.title)
        print(driver.capabilities.get('browserName'))
        driver.quit()


    def test_headless_edge(self):
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless=new")

        driver = webdriver.Edge(options=edge_options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.walmart.com")
        print(driver.capabilities.get('browserName'))
        driver.quit()

    def test_headless_firefox(self):
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("-headless")

        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.walmart.com")
        print(driver.capabilities.get('browserName'))
        driver.quit()


