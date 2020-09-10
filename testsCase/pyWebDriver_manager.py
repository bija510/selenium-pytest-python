#https://pypi.org/project/webdriver-manager/
#pip install webdriver_manager ----> pip list ---> show all the plugin list
#then good to go.....

#####################
#Use with Chrome:
#####################
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

#####################
# Use with FireFox:
#####################
# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#####################
#Use with IE
#####################
# from selenium import webdriver
# from webdriver_manager.microsoft import IEDriverManager
# driver = webdriver.Ie(IEDriverManager().install())

###########################
#Use with Edge or Chromium
###########################
# from selenium import webdriver
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())


driver.get('https://www.facebook.com/')
driver.quit()